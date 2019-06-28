using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using SoulsIds;
using SoulsFormats;
using ESDLang.EzSemble;
using static SoulsIds.GameSpec;
using static SoulsIds.Universe;
using static ESDLang.Script.Util;

namespace ESDLang.Script
{
    class CommandRunner
    {
        private ESDOptions options;
        private ESDOptions.Option opt;
        private GameSpec spec;
        private GameEditor editor;
        private Scraper scraper;
        private Universe u;
        private bool loadedMapData;

        public CommandRunner(ESDOptions options, ESDOptions.Option opt)
        {
            this.options = options;
            this.opt = opt;
            this.spec = options.Spec;
            this.editor = new GameEditor(spec);
            this.scraper = new Scraper(spec);
            this.u = new Universe();
        }

        private class ESDDesc
        {
            public ESD Esd { get; set; }
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
        }
        public void Run()
        {
            string docPath = options.Flag("talk") ? @"dist\ESDScriptingDocumentation_Talk.xml" : @"dist\ESDScriptingDocumentation_Chr.xml";
            if (opt is ESDOptions.Info)
            {
                // Generic info
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
                    string printChr(string chr)
                    {
                        Obj cobj = Obj.ChrModel(chr);
                        if (u.Names.TryGetValue(cobj, out string name)) return $"{chr} ({name})";
                        return chr;
                    }
                    Predicate<ESDDesc> filter = GetFilter();
                    Console.WriteLine($"ESDs{(filter == null ? "" : " with filter")}:");
                    List<ESDDesc> esds = LoadESDs();
                    foreach (ESDDesc esd in esds)
                    {
                        if (filter != null && !filter(esd)) continue;
                        Console.WriteLine($"{(esd.Map == null ? "" : $"{esd.Map}: ")}{esd.Name}.esd{(esd.Chr.Count == 0 ? "" : ": " + string.Join(", ", esd.Chr.Select(c => printChr(c))))}");
                    }
                }
            }
            else if (opt is ESDOptions.WriteBnd bnd)
            {
                if (options.PyInputs.Count == 0) throw new Exception("No Python input files given");
                Predicate<ESDDesc> filter = GetFilter();
                List<ESDDesc> esds = LoadESDs();
                if (esds.Count == 0) throw new Exception("No ESD input files given (through -<game>, -esddir, -i)");
                // TODO: Selection of base esds is really hacky right now... it's not even the case that all ESDs built into a game are compatible with it.
                // See DS3, which has DS2 ESDs in m10_00_00_00.
                ESD baseESD = esds.Last().Esd;
                Dictionary<string, List<ESDDesc>> byName = EsdsByName(esds);
                Predicate<string> esdFilter = GetEsdNameFilter(byName, filter);
                EzSembleContext ezSembleContext = EzSembleContext.LoadFromXml(docPath);
                Dictionary<string, SortedSet<string>> fullPathForBase = new Dictionary<string, SortedSet<string>>();
                foreach (ESDDesc esd in esds)
                {
                    AddMulti(fullPathForBase, esd.FileName, esd.FilePath);
                }
                bool inPrimaryFile(string esdName)
                {
                    if (!byName.ContainsKey(esdName)) return false;
                    foreach (ESDDesc desc in byName[esdName])
                    {
                        if (filter != null && !filter(desc)) continue;
                        if (fullPathForBase.TryGetValue(desc.FileName, out SortedSet<string> fnames) && desc.FilePath == fnames.First()) return true;
                    }
                    return false;
                }
                Dictionary<string, ESD> compiled = new Dictionary<string, ESD>();
                HashSet<string> usedFileNames = new HashSet<string>();
                foreach (string pyFile in options.PyInputs)
                {
                    Dictionary<string, ESD> result = new Compiler(ezSembleContext, options).Compile(pyFile, baseESD, esdFilter);
                    foreach (KeyValuePair<string, ESD> entry in result)
                    {
                        ESD outEsd = entry.Value;
                        // Filtered out
                        if (outEsd == null) continue;
                        string esdName = entry.Key;
                        if (!inPrimaryFile(esdName))
                        {
                            Console.WriteLine($"Not adding {esdName} from {pyFile} - no ESD files to replace");
                            continue;
                        }
                        if (compiled.ContainsKey(esdName))
                        {
                            Console.WriteLine($"Not adding {esdName} from {pyFile} - already added");
                            continue;
                        }
                        compiled[esdName] = outEsd;
                        usedFileNames.Add(byName[esdName].First().FileName);
                        Console.WriteLine($"Adding {esdName} from {pyFile}");
                    }
                }
                Console.WriteLine("---");
                string outDir = GameEditor.AbsolutePath(spec.GameDir, bnd.DirName);
                if (File.Exists(outDir)) throw new Exception($"{outDir} is a file");
                if (!Directory.Exists(outDir)) Directory.CreateDirectory(outDir);
                foreach (KeyValuePair<string, SortedSet<string>> entry in fullPathForBase)
                {
                    string fileName = entry.Key;
                    string baseName = GameEditor.BaseName(fileName);
                    if (fileName.EndsWith(".esd") || fileName.EndsWith(".esd.dcx"))
                    {
                        if (!compiled.ContainsKey(baseName)) continue;
                        DCX.Type dcx = DCX.Type.None;
                        if (fileName.EndsWith(".esd.dcx"))
                        {
                            if (spec.Dcx == DCX.Type.Unknown)
                            {
                                Console.WriteLine($"ERROR: Can't write {fileName} - no -outdcx provided");
                                continue;
                            }
                            dcx = spec.Dcx;
                        }
                        Console.WriteLine($@"Writing {outDir}\{fileName}");
                        compiled[baseName].Write(fileName, dcx);
                    }
                    else if (fileName.EndsWith("esdbnd.dcx"))
                    {
                        if (!usedFileNames.Contains(fileName)) continue;
                        string fullPath = null;
                        foreach (string fullCand in entry.Value)
                        {
                            if (fullPath == null)
                            {
                                fullPath = fullCand;
                                Console.WriteLine($@"Writing {outDir}\{fileName} from {fullPath}");
                                editor.OverrideBnd(fullPath, outDir, compiled, esd => esd.Write());
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
            // it's real 'people who are upset they can't say messed up things with no consequences, as if their absence would be noticed by anyone' hours
            else if (opt is ESDOptions.WriteLoose loose)
            {
                if (options.PyInputs.Count > 0)
                {
                    Predicate<ESDDesc> filter = GetFilter();
                    List<ESDDesc> esds = LoadESDs();
                    if (esds.Count == 0) throw new Exception("At least one ESD input should be given (through -<game>, -esddir, -i) as a template for the others");
                    ESD baseESD = esds.Last().Esd;
                    Predicate<string> esdFilter = GetEsdNameFilter(EsdsByName(esds), filter);
                    EzSembleContext ezSembleContext = EzSembleContext.LoadFromXml(docPath);
                    Dictionary<string, string> esdFiles = new Dictionary<string, string>();
                    foreach (string pyFile in options.PyInputs)
                    {
                        Dictionary<string, ESD> result = new Compiler(ezSembleContext, options).Compile(pyFile, baseESD, esdFilter);
                        foreach (KeyValuePair<string, ESD> entry in result)
                        {
                            ESD outEsd = entry.Value;
                            // Filtered out
                            if (outEsd == null) continue;
                            string esdName = entry.Key;
                            string fname = loose.Template.Replace("%e", esdName);
                            if (esdFiles.ContainsKey(fname))
                            {
                                Console.WriteLine($"Not writing {esdName} to {fname} from {pyFile} - already written");
                                continue;
                            }
                            esdFiles[fname] = pyFile;
                            Console.WriteLine($"Writing {esdName} to {fname} from {pyFile}");
                            outEsd.Write(fname);
                        }
                    }
                }
                else
                {
                    Predicate<ESDDesc> filter = GetFilter();
                    List<ESDDesc> esds = LoadESDs();
                    if (esds.Count == 0) throw new Exception("No ESD input files given (through -<game>, -esddir, -i)");
                    Dictionary<string, string> esdFiles = new Dictionary<string, string>();
                    foreach (ESDDesc esd in esds)
                    {
                        if (filter != null && !filter(esd)) continue;
                        string esdName = esd.Name;
                        string fname = loose.Template.Replace("%e", esdName);
                        if (esdFiles.ContainsKey(fname))
                        {
                            Console.WriteLine($"Not writing {esdName} to {fname} from {esd.FilePath} - already written");
                            continue;
                        }
                        esdFiles[fname] = esd.FilePath;
                        Console.WriteLine($"Writing {esdName} to {fname} from {esd.FilePath}");
                        esd.Esd.Write(fname);
                    }
                }
            }
            else if (opt is ESDOptions.WritePy py)
            {
                string template = py.Template;
                scraper.ScrapeMsgs(u);
                scraper.LoadNames(u);
                scraper.ScrapeItems(u);
                bool hasMap = LoadMapData();
                if (template.Contains("%c") && !hasMap) throw new Exception($"Template uses %c but map data is not available for {spec.Game}");
                Predicate<ESDDesc> filter = GetFilter();
                List<ESDDesc> esds = LoadESDs();
                EzSembleContext ezSembleContext = EzSembleContext.LoadFromXml(docPath);
                HashSet<string> files = new HashSet<string>();
                foreach (ESDDesc esd in esds)
                {
                    if (filter != null && !filter(esd)) continue;
                    string fname = esd.Fill(template);
                    TextWriter writer = null;
                    try
                    {
                        if (fname == "-")
                        {
                            // Keep null to use Console.Out
                            Console.WriteLine("# -*- coding: utf-8 -*-");
                        }
                        else if (!files.Contains(fname))
                        {
                            files.Add(fname);
                            writer = File.CreateText(fname);
                            writer.WriteLine("# -*- coding: utf-8 -*-");
                        }
                        else
                        {
                            writer = File.AppendText(fname);
                        }
                        new Decompiler(ezSembleContext, options, esd.Name, u).Decompile(esd.Esd, writer ?? Console.Out);
                    }
                    finally
                    {
                        if (writer != null) writer.Close();
                    }
                }
            }
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
            return name =>
            {
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
            if (options.Chrs.Count == 0 && options.Maps.Count == 0 && options.Esds.Count == 0) return null;
            if (options.Chrs.Count > 0)
            {
                if (!LoadMapData()) throw new Exception($"chrs used in filter but map data is not available for {spec.Game}");
            }
            return desc =>
            {
                if (options.Chrs.Count > 0 && desc.Chr.Overlaps(options.Chrs)) return true;
                if (options.Maps.Count > 0 && desc.Map != null && options.Maps.Any(map => desc.Map.StartsWith(map))) return true;
                if (options.Esds.Count > 0 && options.Esds.Contains(desc.Name)) return true;
                return false;
            };
        }
        private bool LoadMapData()
        {
            if (spec.Game != FromGame.SDT) return false;
            if (loadedMapData) return true;
            loadedMapData = true;
            return scraper.ScrapeMaps(u);
        }
        private List<ESDDesc> LoadESDs()
        {
            List<string> paths = new List<string>();
            List<ESDDesc> ret = new List<ESDDesc>();
            if (options.EsdInputs.Count > 0)
            {
                paths = options.EsdInputs;
            }
            else if (spec.EsdDir != null)
            {
                string absDir = $@"{spec.GameDir}\{spec.EsdDir}";
                paths = Directory.GetFiles(absDir, "*.esd").Concat(Directory.GetFiles(absDir, "*.esd.dcx").Concat(Directory.GetFiles(absDir, "*esdbnd.dcx"))).ToList();
            }
            foreach (string path in paths)
            {
                if (path.EndsWith(".esd") || path.EndsWith(".esd.dcx"))
                {
                    ret.Add(new ESDDesc
                    {
                        Esd = ESD.Read(path),
                        Name = GameEditor.BaseName(path),
                        FilePath = path,
                        FileName = Path.GetFileName(path),
                    });
                }
                else if (path.EndsWith("esdbnd.dcx"))
                {
                    string map = GameEditor.BaseName(path);
                    foreach (KeyValuePair<string, ESD> esds in editor.LoadBnd(path, (data, name) => ESD.Read(data)))
                    {
                        string esdName = esds.Key;
                        if (esdName.Equals("dummy"))
                        {
                            esdName = $"{map}{esdName}";
                        }
                        ESDDesc desc = new ESDDesc
                        {
                            Esd = esds.Value,
                            Name = esdName,
                            Map = map,
                            FilePath = path,
                            FileName = Path.GetFileName(path),
                        };
                        if (esdName.StartsWith("t") && int.TryParse(esdName.Substring(1), out int esdId))
                        {
                            Obj obj = Obj.Esd(esdId);
                            foreach (Obj part in u.Prev(obj, Verb.CONTAINS, Namespace.PART))
                            {
                                foreach (Obj chr in u.Next(part, Verb.CONTAINS, Namespace.CHR_MODEL))
                                {
                                    desc.Chr.Add(chr.ID);
                                }
                            }
                        }
                        ret.Add(desc);
                    }
                }
                else throw new Exception($"Internal error - {path} is not a known extension");
            }
            return ret;
        }
    }
}
