using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Security.Cryptography;
using SoulsIds;
using SoulsFormats;
using ESDLang.EzSemble;
using ESDLang.Doc;
using static SoulsIds.GameSpec;
using static SoulsIds.Universe;
using static ESDLang.Script.Util;
using static ESDLang.Script.EDDText;
using ESDLang.DLSE;

namespace ESDLang.Script
{
    class CommandRunner
    {
        private ESDOptions options;
        private ESDOptions.Option opt;
        private GameSpec spec;
        private GameEditor editor;
        private readonly Scraper scraper;
        private readonly Universe u;
        private bool loadedMapData;
        private Dictionary<(ESDOptions.CmdType, FromGame), EzSembleContext> contextCache = new();

        // An instance is created per command, meaning game-specific things are fixed at this point.
        public CommandRunner(ESDOptions options, ESDOptions.Option opt)
        {
            this.options = options;
            this.opt = opt;
            this.spec = options.Spec;
            this.editor = new GameEditor(spec);
            this.scraper = new Scraper(spec, options.ModDir);
            this.u = new Universe();
        }

        private class ESDDesc
        {
            public ESD Esd { get; set; }
            public ESDDLSE EsdOld { get; set; }
            public string Hash { get; set; }
            public string FilePath { get; set; }
            public string FileName { get; set; }
            public string Name { get; set; }
            public string Map { get; set; }
            public SortedSet<string> Chr = new SortedSet<string>();

            public string Fill(string template)
            {
                string map = Map ?? "unk";
                string chr = Chr.Count == 0 ? "unk" : Chr.First();
                return template.Replace("%e", Name).Replace("%m", map).Replace("%c", chr);
            }

            public ESDDesc ForExtraESD(string name)
            {
                return new ESDDesc
                {
                    FilePath = FilePath,
                    FileName = FileName,
                    Name = name,
                };
            }
        }

        private EzSembleContext LoadContext(ESDOptions.CmdType type, FromGame game)
        {
            if (contextCache.TryGetValue((type, game), out EzSembleContext context)) return context;
            string docPath = $@"dist\ESDScriptingDocumentation_{type}.xml";
            context = contextCache[(type, game)] = EzSembleContext.LoadFromXml(docPath);
            docPath = $@"dist\ESDScriptingDocumentation_{(type == ESDOptions.CmdType.TalkER ? ESDOptions.CmdType.Talk : type)}.json";
            context.Doc = ESDDocumentation.DeserializeFromFile(docPath, new ESDDocumentation.DocOptions { Game = game.ToString().ToLowerInvariant() });
            return context;
        }

        private EzSembleContext LoadContext(string esdName, FromGame game)
        {
            return LoadContext(options.Type == ESDOptions.CmdType.Unknown ? ESDName.GetCmdType(Path.GetFileNameWithoutExtension(esdName), game) : options.Type, game);
        }

        private static readonly List<FromGame> oodleGames = new() { FromGame.SDT, FromGame.ER, FromGame.AC6, FromGame.NR };

        public void Run()
        {
            bool backup = options.Flag("backup");
            void MaybeBackup(string path)
            {
                string bak = path + ".bak";
                if (backup && File.Exists(path) && !File.Exists(bak))
                {
                    Console.WriteLine($"Creating {Path.GetFileName(bak)}");
                    File.Copy(path, bak);
                }
            }
            // Hacky oodle copy
            List<string> oodles = new() { "oo2core_6_win64.dll", "oo2core_8_win64.dll", "oo2core_9_win64.dll" };
            if (oodleGames.Contains(spec.Game) && spec.GameDir != null && !oodles.Any(File.Exists))
            {
                foreach (string oodle in oodles)
                {
                    if (File.Exists(Path.Combine(spec.GameDir, oodle)))
                    {
                        File.Copy(Path.Combine(spec.GameDir, oodle), oodle);
                        break;
                    }
                }
            }
            if (opt is ESDOptions.Info)
            {
                // Generic info. This is of limited utility. It can show known files without having to unpack them all.
                if (options.PyInputs.Count > 0)
                {
                    // Parse files. If there are any filters, activate those.
                }
                else
                {
                    // Just get ESD names from bnds. Also apply filters.
                    scraper.ScrapeMsgs(u);
                    scraper.LoadNames(u);
                    LoadMapData();
                    int charaDivisor = spec.Game < FromGame.DS3 ? 10 : 50;
                    string printChr(string chr)
                    {
                        Obj cobj = Obj.ChrModel(chr);
                        if (u.Names.TryGetValue(cobj, out string name)) return $"{chr} ({name})";
                        if (chr.StartsWith("h") && int.TryParse(chr.Substring(1), out int id) && u.Names.TryGetValue(Obj.Npc(id / charaDivisor * charaDivisor), out string name2)) return $"{chr} ({name2})";
                        return chr;
                    }
                    Predicate<ESDDesc> filter = GetFilter();
                    Console.WriteLine($"ESDs{(filter == null ? "" : " with filter")}:");
                    List<ESDDesc> esds = GetESDs(filter, parse: false, check: true);
                    foreach (ESDDesc esd in esds)
                    {
                        if (filter != null && !filter(esd)) continue;
                        Console.WriteLine($"{(esd.Map == null ? "" : $"{esd.Map}: ")}{esd.Name}.esd: {esd.Hash.Substring(0, 8)}{(esd.Chr.Count == 0 ? "" : $", " + string.Join(", ", esd.Chr.Select(c => printChr(c))))}");
                    }
                }
            }
            else if (opt is ESDOptions.WriteBnd bnd)
            {
                if (options.PyInputs.Count == 0) throw new Exception("No Python input files given");
                if (options.Game == FromGame.UNKNOWN) throw new Exception($"Game not specified");
                if (options.Game == FromGame.DES) throw new Exception("Write for DeS not yet supported");
                bool copySame = options.Flag("copysame");
                Predicate<ESDDesc> filter = GetFilter();
                List<ESDDesc> esds = GetESDs(filter, parse: true, check: copySame);
                // TODO: Selection of base esds is really hacky right now... it's not even the case that all ESDs built into a game are compatible with it.
                // See DS3, which has DS2 ESDs in m10_00_00_00.
                ESDDesc baseDesc = esds.Where(d => d.Esd != null).LastOrDefault();
                if (baseDesc == null) throw new Exception("No ESD input files given (through -<game>, -esddir, -i)");
                Dictionary<string, List<ESDDesc>> byHash = new Dictionary<string, List<ESDDesc>>();
                foreach (ESDDesc esd in esds)
                {
                    if (esd.Hash != null) AddMulti(byHash, esd.Hash, esd);
                }
                Dictionary<string, List<ESDDesc>> byName = EsdsByName(esds);
                Predicate<string> esdFilter = GetEsdNameFilter(byName, filter);
                Dictionary<string, SortedSet<string>> fullPathForBase = new Dictionary<string, SortedSet<string>>();
                foreach (ESDDesc esd in esds)
                {
                    AddMulti(fullPathForBase, esd.FileName, esd.FilePath);
                }
                HashSet<string> eligibleFullPaths = new(fullPathForBase.Values.Select(fnames => fnames.First()));
                // For each extra ESD, find a bnd to associate it with
                foreach ((string esdName, string bndName) in options.ExtraEsds)
                {
                    // Match the condition used by inPrimaryFile
                    ESDDesc match = esds.Find(e => GameEditor.BaseName(e.FileName) == bndName && eligibleFullPaths.Contains(e.FilePath));
                    if (match != null)
                    {
                        AddMulti(byName, esdName, match.ForExtraESD(esdName));
                    }
                }
                bool inPrimaryFile(string esdName)
                {
                    if (!byName.ContainsKey(esdName)) return false;
                    foreach (ESDDesc desc in byName[esdName])
                    {
                        if (filter != null && !filter(desc)) continue;
                        if (eligibleFullPaths.Contains(desc.FilePath)) return true;
                    }
                    return false;
                }
                Dictionary<string, ESD> compiled = new Dictionary<string, ESD>();
                HashSet<string> usedFileNames = new HashSet<string>();
                List<string> pyFiles = new List<string>();
                // Add our own wildcard feature because WSL completely melts down getting 200 files at once, like a complete chump
                foreach (string pyFile in options.PyInputs)
                {
                    if (pyFile.Contains("*"))
                    {
                        pyFiles.AddRange(Directory.GetFiles(Path.GetDirectoryName(pyFile), Path.GetFileName(pyFile)));
                    }
                    else
                    {
                        pyFiles.Add(pyFile);
                    }
                }
                foreach (string pyFile in pyFiles)
                {
                    // Console.WriteLine($"Compiling {pyFile}");
                    Dictionary<string, ESD> result = new Compiler(LoadContext(pyFile, options.Game), options).Compile(pyFile, baseDesc.Esd, esdFilter);
                    // There was an error. An error message was printed
                    if (result == null) throw new Exception($"Failed to compile {pyFile}");
                    foreach (KeyValuePair<string, ESD> entry in result)
                    {
                        ESD outEsd = entry.Value;
                        // Filtered out
                        if (outEsd == null) continue;
                        string esdName = ESDName.FromFunctionPrefix(entry.Key);
                        if (!inPrimaryFile(esdName))
                        {
                            Console.WriteLine($"Not adding {esdName} from {pyFile} - no ESD files to replace/add");
                            continue;
                        }
                        if (compiled.ContainsKey(esdName))
                        {
                            Console.WriteLine($"Not adding {esdName} from {pyFile} - already added");
                            continue;
                        }
                        Console.WriteLine($"Adding {esdName} from {pyFile}");
                        compiled[esdName] = outEsd;
                        ESDDesc desc = byName[esdName].First();
                        usedFileNames.Add(desc.FileName);
                    }
                }
                foreach (KeyValuePair<string, ESD> entry in compiled.ToList())
                {
                    ESDDesc desc = byName[entry.Key].First();
                    if (desc.Hash != null && byHash.TryGetValue(desc.Hash, out List<ESDDesc> dupes))
                    {
                        foreach (ESDDesc dupe in dupes)
                        {
                            if (compiled.ContainsKey(dupe.Name)) continue;
                            Console.WriteLine($"Adding {dupe.Name} as a dupe of {entry.Key}");
                            compiled[dupe.Name] = entry.Value;
                            usedFileNames.Add(dupe.FileName);
                        }
                    }
                }
                Console.WriteLine("---");
                string outDir;
                if (bnd.DirName != null)
                {
                    // This previously used GameEditor.AbsolutePath
                    outDir = bnd.DirName;
                    if (File.Exists(outDir)) throw new Exception($"-writebnd argument {outDir} is not a directory");
                    if (!Directory.Exists(outDir)) Directory.CreateDirectory(outDir);
                }
                else
                {
                    string outPath = bnd.FileName;
                    FileInfo outInfo = new FileInfo(outPath);
                    outDir = outInfo.DirectoryName;
                    if (!(usedFileNames.Count == 1 && usedFileNames.First() == outInfo.Name))
                    {
                        Console.WriteLine($"Restricting output to {outInfo.Name}");
                        usedFileNames = new HashSet<string> { outInfo.Name };
                    }
                }
                foreach (KeyValuePair<string, SortedSet<string>> entry in fullPathForBase)
                {
                    string fileName = entry.Key;
                    string baseName = GameEditor.BaseName(fileName);
                    DCX.Type dcx = DCX.Type.None;
                    if (fileName.EndsWith(".dcx"))
                    {
                        if (spec.Dcx == DCX.Type.Unknown)
                        {
                            // TODO: This can be kept as-is without changing the compression type, surely
                            throw new Exception($"Can't write {fileName} - no -outdcx provided");
                        }
                        dcx = spec.Dcx;
                    }
                    if (fileName.EndsWith(".esd") || fileName.EndsWith(".esd.dcx"))
                    {
                        // Can just use writeloose but this could be useful for mixed games.
                        if (!compiled.ContainsKey(baseName)) continue;
                        if (!usedFileNames.Contains(fileName)) continue;
                        string outPath = $@"{outDir}\{fileName}";
                        MaybeBackup(outPath);
                        Console.WriteLine($@"Writing {outPath}");
                        compiled[baseName].Write(outPath, dcx);
                    }
                    else if (fileName.EndsWith("esdbnd.dcx") || fileName.EndsWith("esdbnd"))
                    {
                        if (!usedFileNames.Contains(fileName)) continue;
                        string fullPath = null;
                        foreach (string fullCand in entry.Value)
                        {
                            if (fullPath == null)
                            {
                                fullPath = fullCand;
                                string outPath = $@"{outDir}\{Path.GetFileName(fullPath)}";
                                MaybeBackup(outPath);
                                Console.WriteLine($@"Writing {fullPath} -> {outDir}\{fileName}");
                                IBinder outBnd = editor.GetOverrideBndRel(fullPath, compiled, esd => esd.Write());
                                if (options.ExtraEsds.Count > 0)
                                {
                                    List<string> extraEsds = options.ExtraEsds
                                        .Where(e => e.Value == baseName && compiled.ContainsKey(e.Key))
                                        .Select(e => e.Key)
                                        .ToList();
                                    if (extraEsds.Count > 0)
                                    {
                                        // We are way out of our depth. Try to copy someone else's homework
                                        BinderFile victim = outBnd.Files.Find(f => f.Name.EndsWith(".esd"));
                                        if (victim == null) throw new Exception($"Can't pack extra ESDs using {fullPath}: no existing .esd files found within");
                                        string bndPath = victim.Name.Substring(0, victim.Name.LastIndexOfAny(new[] { '/', '\\' }) + 1);
                                        foreach (string extra in extraEsds)
                                        {
                                            Console.WriteLine($"Adding extra ESD {extra} to {baseName}");
                                            ESD outEsd = compiled[extra];
                                            outBnd.Files.Add(new BinderFile
                                            {
                                                Flags = victim.Flags,
                                                CompressionType = victim.CompressionType,
                                                Name = bndPath + extra + ".esd",
                                                Bytes = outEsd.Write(),
                                            });
                                        }
                                        int id = 0;
                                        foreach (BinderFile file in outBnd.Files)
                                        {
                                            file.ID = id++;
                                        }
                                    }
                                }
                                editor.WriteBnd(outPath, outBnd, dcx);
                            }
                            else
                            {
                                Console.WriteLine($"Skipping {fullCand}");
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine($"ERROR: Unrecognized file {fileName}");
                    }
                }
            }
            else if (opt is ESDOptions.WriteLoose loose)
            {
                if (options.Game == FromGame.UNKNOWN) throw new Exception($"Game not specified");
                if (options.Game == FromGame.DES) throw new Exception("Write for DeS not yet supported");
                if (options.PyInputs.Count > 0)
                {
                    Predicate<ESDDesc> filter = GetFilter();
                    // Note: In this case, only one of the ESDs needs to be parsed.
                    List<ESDDesc> esds = GetESDs(filter, parse: true, check: false);
                    ESDDesc baseDesc = esds.Where(d => d.Esd != null).LastOrDefault();
                    if (baseDesc == null) throw new Exception("At least one ESD input should be given (through -<game>, -esddir, -i) as a template for the others");
                    Predicate<string> esdFilter = GetEsdNameFilter(EsdsByName(esds), filter);
                    Dictionary<string, string> esdFiles = new Dictionary<string, string>();
                    foreach (string pyFile in options.PyInputs)
                    {
                        Dictionary<string, ESD> result = new Compiler(LoadContext(pyFile, options.Game), options).Compile(pyFile, baseDesc.Esd, esdFilter);
                        if (result == null) throw new Exception($"Failed to compile {pyFile}");
                        foreach (KeyValuePair<string, ESD> entry in result)
                        {
                            ESD outEsd = entry.Value;
                            // Filtered out
                            if (outEsd == null) continue;
                            string esdName = ESDName.FromFunctionPrefix(entry.Key);
                            string outPath = loose.Template.Replace("%e", esdName);
                            if (esdFiles.ContainsKey(outPath))
                            {
                                Console.WriteLine($"Not writing {pyFile}:{esdName} -> {outPath} - already written");
                                continue;
                            }
                            esdFiles[outPath] = pyFile;
                            MaybeBackup(outPath);
                            Console.WriteLine($"Writing {pyFile}:{esdName} -> {outPath}");
                            outEsd.Write(outPath);
                        }
                    }
                }
                else
                {
                    Predicate<ESDDesc> filter = GetFilter();
                    List<ESDDesc> esds = GetESDs(filter, parse: true, check: false);
                    if (esds.Count == 0) throw new Exception("No ESD input files given (through -<game>, -esddir, -i)");
                    Dictionary<string, string> esdFiles = new Dictionary<string, string>();
                    foreach (ESDDesc esd in esds)
                    {
                        if (filter != null && !filter(esd)) continue;
                        string esdName = esd.Name;
                        string outPath = loose.Template.Replace("%e", esdName);
                        if (esdFiles.ContainsKey(outPath))
                        {
                            Console.WriteLine($"Not writing {esd.FilePath}:{esdName} -> {outPath} - already written");
                            continue;
                        }
                        esdFiles[outPath] = esd.FilePath;
                        MaybeBackup(outPath);
                        Console.WriteLine($"Writing {esd.FilePath}:{esdName} -> {outPath}");
                        esd.Esd.Write(outPath);
                    }
                }
            }
            else if (opt is ESDOptions.WritePy py)
            {
                if (options.Game == FromGame.UNKNOWN) throw new Exception($"Game not specified");
                string template = py.Template;
                bool hasMap = false;
                if (options.Flag("annotate"))
                {
                    scraper.ScrapeMsgs(u);
                    scraper.LoadNames(u);
                    scraper.ScrapeItems(u);
                    hasMap = LoadMapData();
                }
                if (template.Contains("%c") && !hasMap) throw new Exception($"Template uses %c but map data is not available for {spec.Game}");
                string eddDir = null;
                if (options.EddDir != null)
                {
                    eddDir = WindowsifyPath(options.EddDir);
                    if (!Directory.Exists(eddDir)) throw new Exception($"EDD directory {eddDir} does not exist");
                }
                else if (options.Game == FromGame.DS2S)
                {
                    eddDir = @"dist\DS2S\EDD";
                }
                Predicate<ESDDesc> filter = GetFilter();
                List<ESDDesc> esds = GetESDs(filter, parse: true, check: false);
                HashSet<string> files = new HashSet<string>();
                Dictionary<string, List<string>> filesByEsdName = new Dictionary<string, List<string>>();
                foreach (ESDDesc esd in esds)
                {
                    if (filter != null && !filter(esd)) continue;
                    string outPath = esd.Fill(template);
                    if (!filesByEsdName.TryGetValue(esd.Name, out List<string> nameFiles))
                    {
                        filesByEsdName[esd.Name] = nameFiles = new List<string>();
                    }
                    if (nameFiles.Contains(outPath))
                    {
                        // This happens in DS1 with t100000 in m10_00_00_00 and 12_00_00_01.
                        // We could also check for content duplication or not. Actual differences may deserve a full error.
                        Console.WriteLine($"Warning: Won't write ESD duplicate {esd.Name} to {outPath} multiple times. It is found in these files:");
                        foreach (string dupePath in esds.Where(e => e.Name == esd.Name).Select(e => e.FilePath))
                        {
                            Console.WriteLine(dupePath);
                        }
                        continue;
                    }
                    nameFiles.Add(outPath);
                    if (outPath != "-")
                    {
                        // Just in this case, also create directories, since it's a common use case to dump to a new directory
                        string dirName = Path.GetDirectoryName(outPath);
                        if (!string.IsNullOrWhiteSpace(dirName) && !File.Exists(dirName) && !Directory.Exists(dirName))
                        {
                            Directory.CreateDirectory(dirName);
                        }
                        MaybeBackup(outPath);
                        Console.WriteLine($"Writing {esd.FilePath}:{esd.Name} -> {outPath}");
                    }
                    // Try to find EDD for DS2
                    EDDText edd = null;
                    if (eddDir != null)
                    {
                        string eddPath = $@"{eddDir}\{esd.Name}.edd";
                        if (File.Exists(eddPath))
                        {
                            edd = new EDDText();
                            edd.ReadEDD(eddPath);
                        }
                        if (File.Exists(eddPath + ".txt"))
                        {
                            edd = new EDDText();
                            edd.ReadTxt(eddPath + ".txt");
                        }
                    }
                    TextWriter writer = null;
                    try
                    {
                        if (outPath == "-")
                        {
                            // Keep null to use Console.Out
                            Console.WriteLine("# -*- coding: utf-8 -*-");
                        }
                        else if (!files.Contains(outPath))
                        {
                            files.Add(outPath);
                            writer = File.CreateText(outPath);
                            writer.WriteLine("# -*- coding: utf-8 -*-");
                        }
                        else
                        {
                            writer = File.AppendText(outPath);
                        }
                        Decompiler decomp = new Decompiler(LoadContext(esd.Name, options.Game), options, ESDName.ToFunctionPrefix(esd.Name), u, edd?.edd);
                        decomp.Decompile((object)esd.Esd ?? esd.EsdOld, writer ?? Console.Out);
                        // Experimental graph option, TODO finish this and add options for it
                        // new Grapher(u, decomp).Graph(esd.Esd, "x38"); // x9 subconds, x4 ch3, x7 much dialogue
                        // new Grapher(u, decomp).Graph(esd.EsdOld, "1"); // x9 subconds, x4 ch3, x7 much dialogue
                    }
                    finally
                    {
                        if (writer != null) writer.Close();
                    }
                }
            }
            else if (opt is ESDOptions.WriteEdd edd)
            {
                if (backup) throw new Exception($"Backup not supported for writing EDDs");
                // This used to parse ESDs but this is really not necessary here. Just use makeshift ESDDescs if filters are needed.
                Predicate<ESDDesc> filter = GetFilter();
                if (options.EddDir == null) throw new Exception("No -edddir given with -writeedd");

                EDDFormat format = options.EddFormat;
                List<string> sharedStrings = format == EDDFormat.Flat ? null : new List<string>();
                if (format == EDDFormat.Join && sharedStrings.Count == 0)
                {
                    ReadEddStrs(options.EddDir, sharedStrings);
                    Console.WriteLine($"Read {sharedStrings.Count} strings from {options.EddDir}");
                }
                Dictionary<string, EDDText> texts = new Dictionary<string, EDDText>();
                List<string> eddPaths = Directory.GetFiles(options.EddDir, "*.edd").Concat(Directory.GetFiles(options.EddDir, "*.edd.txt")).ToList();
                foreach (string path in eddPaths)
                {
                    string name = GameEditor.BaseName(path);
                    ESDDesc desc = new ESDDesc { Name = name };
                    if (filter != null && !filter(desc)) continue;
                    // Read in EDDs
                    if (format == EDDFormat.Flat || format == EDDFormat.Chunk)
                    {
                        EDDText text = new EDDText();
                        text.ReadEDD(path, sharedStrings);
                        texts[name] = text;
                    }
                    else if (format == EDDFormat.Join)
                    {
                        EDDText text = new EDDText();
                        text.ReadTxt(path, sharedStrings);
                        texts[name] = text;
                    }
                }
                // Write them
                if (format == EDDFormat.Chunk)
                {
                    string dir = Path.GetDirectoryName(edd.Template);
                    Console.WriteLine($"Dumping strings to {dir}");
                    WriteEddStrs(dir, sharedStrings, 500);
                }
                Dictionary<string, string> esdFiles = new Dictionary<string, string>();
                foreach ((string name, EDDText text) in texts)
                {
                    string fname = edd.Template.Replace("%e", name);
                    if (esdFiles.ContainsKey(fname))
                    {
                        Console.WriteLine($"Not dumping {name} -> {fname} - already written");
                        continue;
                    }
                    Console.WriteLine($"Dumping {name} -> {fname}");
                    text.Write(fname, format);
                    esdFiles[fname] = fname;
                }
            }
            else throw new Exception($"Internal error: non-actionable option {opt}");
        }

        private static Dictionary<string, List<ESDDesc>> EsdsByName(List<ESDDesc> esds)
        {
            Dictionary<string, List<ESDDesc>> byName = new Dictionary<string, List<ESDDesc>>();
            foreach (ESDDesc esd in esds)
            {
                AddMulti(byName, esd.Name, esd);
            }
            return byName;
        }

        private static Predicate<string> GetEsdNameFilter(Dictionary<string, List<ESDDesc>> byName, Predicate<ESDDesc> baseFilter)
        {
            if (baseFilter == null) return null;
            return partName =>
            {
                string name = ESDName.FromFunctionPrefix(partName);
                if (!byName.ContainsKey(name)) return false;
                foreach (ESDDesc esd in byName[name])
                {
                    if (baseFilter(esd)) return true;
                }
                return false;
            };
        }

        private Predicate<ESDDesc> GetFilter()
        {
            if (options.ChrFilters.Count == 0 && options.MapFilters.Count == 0 && options.EsdFilters.Count == 0) return null;
            if (options.ChrFilters.Count > 0)
            {
                if (!LoadMapData()) throw new Exception($"chrs used in filter but map data is not available for {spec.Game}");
            }
            return desc =>
            {
                if (options.ChrFilters.Count > 0 && desc.Chr.Overlaps(options.ChrFilters)) return true;
                if (options.MapFilters.Count > 0 && desc.Map != null && options.MapFilters.Any(map => desc.Map.StartsWith(map))) return true;
                if (options.EsdFilters.Count > 0 && options.EsdFilters.Any(name => desc.Name.StartsWith(name))) return true;
                return false;
            };
        }

        private bool LoadMapData()
        {
            if (loadedMapData) return true;
            loadedMapData = true;
            return scraper.ScrapeMaps(u);
        }

        private List<ESDDesc> GetESDs(Predicate<ESDDesc> filter, bool parse, bool check)
        {
            bool load = parse || check;
            List<string> paths = new List<string>();
            List<ESDDesc> ret = new List<ESDDesc>();
            ESDDesc makeDesc(string path, string name = null, string map = null)
            {
                return new ESDDesc
                {
                    Name = name ?? GameEditor.BaseName(path),
                    Map = map,
                    FilePath = path,
                    FileName = Path.GetFileName(path),
                };
            }
            // If no data, and loads are called for, path will be used instead.
            void loadDesc(ESDDesc desc, string path, byte[] data = null)
            {
                if (load && (filter == null || filter(desc)))
                {
                    if (data == null)
                    {
                        data = File.ReadAllBytes(path);
                        data = DCX.Is(data) ? DCX.Decompress(data) : data;
                    }
                    if (parse)
                    {
                        // Slightly hacky, is there a better way to pass this information?
                        if (spec.Game == FromGame.DES)
                        {
                            desc.EsdOld = ESDDLSE.Read(data);
                        }
                        else
                        {
                            desc.Esd = ESD.Read(data);
                        }
                    }
                    if (check)
                    {
                        desc.Hash = GetMD5Hash(data);
                    }
                }
            }
            if (options.EsdInputs.Count > 0)
            {
                paths = options.EsdInputs;
            }
            else if (spec.EsdDir != null)
            {
                string absDir = GameEditor.AbsolutePath(spec.GameDir, spec.EsdDir);
                paths = Directory.GetFiles(absDir, "*.esd").Concat(Directory.GetFiles(absDir, "*.esd.dcx")).Concat(Directory.GetFiles(absDir, "*esdbnd.dcx")).Concat(Directory.GetFiles(absDir, "*esdbnd")).ToList();
            }
            foreach (string inPath in paths)
            {
                string path = WindowsifyPath(inPath);
                Console.WriteLine($"Loading {path}");
                if (path.EndsWith(".esd") || path.EndsWith(".esd.dcx"))
                {
                    ESDDesc desc = makeDesc(path);
                    loadDesc(desc, path);
                    ret.Add(desc);
                }
                // Not an extension exactly - the real extensions are chresdbnd and talkesdbnd.
                else if (path.EndsWith("esdbnd.dcx") || path.EndsWith("esdbnd"))
                {
                    string map = GameEditor.BaseName(path);
                    foreach (KeyValuePair<string, byte[]> esds in editor.LoadBnd(path, (data, name) => load ? data : null))
                    {
                        string esdName = esds.Key;
                        // Special processing, because multiple ESDs are named dummy. They are parsed out correctly again later.
                        if (esdName.Equals("dummy"))
                        {
                            esdName = $"{esdName}_{map}";
                        }
                        ESDDesc desc = makeDesc(path, esdName, map);
                        if (esdName.StartsWith("t") && int.TryParse(esdName.Substring(1), out int esdId))
                        {
                            Obj obj = Obj.Esd(esdId);
                            foreach (Obj part in u.Prev(obj, Verb.CONTAINS, Namespace.Part))
                            {
                                foreach (Obj chr in u.Next(part, Verb.CONTAINS, Namespace.ChrModel))
                                {
                                    desc.Chr.Add(chr.ID);
                                }
                                foreach (Obj npc in u.Next(part, Verb.CONTAINS, Namespace.Human))
                                {
                                    if (int.TryParse(npc.ID, out int id)) desc.Chr.Add("h" + npc.ID);
                                }
                            }
                        }
                        loadDesc(desc, path, esds.Value);
                        ret.Add(desc);
                    }
                }
                else throw new Exception($"Internal error - {path} is not a known extension");
            }
            return ret;
        }

        private static readonly MD5 MD5 = MD5.Create();
        private static string GetMD5Hash(byte[] data)
        {
            // Ignore trivial differences between ESDs: Unk70 fields and the name at the end.
            // This will get a bit hacky but we don't want to parse the whole ESD to do this.
            if (data.Length >= 0x80) Array.Clear(data, 0x70, 0x10);
            BinaryReaderEx br = new BinaryReaderEx(false, data);
            br.VarintLong = br.AssertASCII("fSSL", "fsSL", "DLSE") == "fsSL";
            br.Position = 0x80;
            if (br.VarintLong) br.AssertInt32(0);
            br.ReadVarint();
            br.ReadVarint();
            int offset = 0x6C + (int)br.ReadVarint();
            byte[] hash = MD5.ComputeHash(data, 0, Math.Min(data.Length, offset));
            return string.Join("", hash.Select(x => $"{x:x2}"));
        }
    }
}
