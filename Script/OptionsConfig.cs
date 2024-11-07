using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using SoulsIds;
using static SoulsIds.GameSpec;
using System.Runtime;

namespace ESDLang.Script
{
    class OptionsConfig
    {
        // Simple JSON representation of ESDOptions.
        // This is required for Yabber-style drag-and-drop runs. It is a strict subset of command line functionality.
        [JsonProperty(PropertyName = "game")]
        public string Game { get; set; }
        [JsonProperty(PropertyName = "basedir")]
        public string BaseDir { get; set; }
        [JsonProperty(PropertyName = "moddir")]
        public string ModDir { get; set; }
        [JsonProperty(PropertyName = "backup")]
        public bool Backup { get; set; }
        [JsonProperty(PropertyName = "extra")]
        public Dictionary<string, string> ExtraESDs { get; set; }
        [JsonProperty(PropertyName = "other_options")]
        public string Options { get; set; }

        // If BaseDir and ModDir are set, new files to copy from the BaseDir and then decompile
        [JsonIgnore]
        public Dictionary<string, string> Decompile { get; set; } = new();

        private static OptionsConfig ReadExistingConfig(string configPath)
        {
            try
            {
                OptionsConfig readConfig = JsonConvert.DeserializeObject<OptionsConfig>(File.ReadAllText(configPath));
                Console.WriteLine($"Using config {configPath}");
                Console.WriteLine();
                return readConfig;
            }
            catch (JsonException ex)
            {
                throw new Exception($"Failed to parse {configPath}. Please either fix it or delete it so it can be recreated.", ex);
            }
        }

        public static OptionsConfig GetOrCreate(List<string> files)
        {
            // If given no files, or a project.json/esdtoolconfig.json file, files to decompile should also be prompted.
            bool promptDecompile = false;
            if (files.Count == 0)
            {
                promptDecompile = true;
            }
            string argConfigPath = null;
            string argProjectPath = null;
            files.RemoveAll(path =>
            {
                string name = Path.GetFileName(path);
                if (name == "project.json")
                {
                    promptDecompile = true;
                    argProjectPath ??= path;
                    return true;
                }
                if (name == "esdtoolconfig.json")
                {
                    promptDecompile = true;
                    argConfigPath ??= path;
                    return true;
                }
                return false;
            });
            string configPath = argConfigPath;
            string inputFile = files.FirstOrDefault();
            if (configPath == null && inputFile != null)
            {
                string configDir = Path.GetDirectoryName(inputFile);
                configPath = Path.Combine(configDir, "esdtoolconfig.json");
            }

            if (promptDecompile)
            {
                Console.WriteLine($"Welcome to esdtool.");
                Console.WriteLine($"You've initiated a setup process to copy ESDs from the game directory into a mod-specific");
                Console.WriteLine($"project directory and then decompile them. If you want to compile/decompile files without");
                Console.WriteLine($"copying anything, close this window and drag those files into esdtool.exe directly instead.");
                Console.WriteLine();
            }

            OptionsConfig config = new();
            if (configPath != null)
            {
                configPath = new FileInfo(configPath).FullName;
                if (File.Exists(configPath))
                {
                    // All data is already provided, and can be returned if nothing else is needed.
                    config = ReadExistingConfig(configPath);
                }
                else
                {
                    Console.WriteLine($"Creating {configPath}");
                    Console.WriteLine();
                }
            }

            bool firstTimeRun = !File.Exists(configPath);

            bool promptYesNo()
            {
                string text = Console.ReadLine();
                if (text == null) throw new IOException("Input error");
                return text.Trim().ToLowerInvariant().StartsWith("y");
            }
            void promptAny()
            {
                string text = Console.ReadLine();
                if (text == null) throw new IOException("Input error");
            }

            // Prompt for project file if needed
            ProjectSettingsFile project = null;
            if (config.Game == null || config.BaseDir == null && (promptDecompile && string.IsNullOrWhiteSpace(config.ModDir)))
            {
                if (argProjectPath != null)
                {
                    project = ProjectSettingsFile.LoadProjectFile(argProjectPath);
                }
                else
                {
                    while (true)
                    {
                        Console.Write($"Select a project.json file to load game and mod info [y/n]? ");
                        if (!promptYesNo())
                        {
                            Console.WriteLine();
                            break;
                        }
                        string defaultDir = null;
                        if (configPath != null && !ProjectSettingsFile.TryGetProjectFile(configPath, out string projectPath))
                        {
                            defaultDir = Path.GetDirectoryName(projectPath);
                        }
                        if (FileDialog.OpenFileDialog(new[] { "json" }, out string selected, defaultDir))
                        {
                            Console.WriteLine();
                            project = ProjectSettingsFile.LoadProjectFile(selected);
                            if (project.Game != FromGame.UNKNOWN)
                            {
                                break;
                            }
                            else
                            {
                                Console.WriteLine($"Project file \"{project.FilePath}\" does not seem to have a game supported by esdtool.");
                                Console.WriteLine();
                                project = null;
                            }
                        }
                    }
                }
            }
            if (project != null)
            {
                // Load basic data from there. ModDir requires knowing where decompiled files are; find that later.
                config.Game = project.Game.ToString().ToLowerInvariant();
                config.BaseDir = project.GameDir;
            }

            while (config.Game == null || !ESDOptions.Games.Names.ContainsKey(config.Game))
            {
                Console.WriteLine($"Supported games: [{string.Join(", ", ESDOptions.Games.Names.Keys)}]");
                Console.Write("Select a game type: ");
                string text = Console.ReadLine();
                if (text == null) return null;
                text = text.Trim().ToLowerInvariant();
                Console.WriteLine();
                if (!ESDOptions.Games.Names.ContainsKey(text))
                {
                    Console.WriteLine($"Error: Unrecognized game type \"{text}\"");
                    Console.WriteLine();
                    continue;
                }
                config.Game = text;
            }
            GameSpec gameInfo = ForGame(ESDOptions.Games.Names[config.Game]);

            if (config.BaseDir == null)
            {
                string baseDir = gameInfo.GameDir;
                if (Directory.Exists(baseDir))
                {
                    Console.WriteLine($"Detected game directory: {baseDir}");
                    Console.WriteLine("Make sure to unpack your game with UXM/UDSFM first.");
                    Console.Write($"Use this directory [y/n]? ");
                    if (!promptYesNo())
                    {
                        baseDir = null;
                    }
                    Console.WriteLine();
                }
                else
                {
                    baseDir = null;
                }
                while (baseDir == null)
                {
                    Console.Write("Unpack your game with UXM/UDSFM and press enter to select a game directory. ");
                    promptAny();
                    if (FileDialog.OpenFolderDialog(out string path))
                    {
                        Console.WriteLine();
                        if (Directory.Exists(path))
                        {
                            baseDir = path;
                        }
                        else
                        {
                            Console.WriteLine($"Error: Directory \"{path}\" not found");
                            Console.WriteLine();
                        }
                    }
                }
                config.BaseDir = Path.GetFullPath(baseDir);
            }

            // Mod directory has a few odd cases if unset. Try to ask as few questions as possible.
            // If both project and configPath exist, it can be automatically calculated.
            // If not promptDecompile, it can be optionally queried.
            // If promptDecompile and no project, it must be queried.
            // Finally actually prompt game files.
            // Make the path relative if possible.
            if (project != null)
            {
                config.ModDir = project.ModDir;
            }
            while (string.IsNullOrWhiteSpace(config.ModDir) && (promptDecompile || firstTimeRun))
            {
                if (promptDecompile)
                {
                    Console.Write("Press enter to select the top-level mod directory to decompile vanilla files into. ");
                    promptAny();
                }
                else
                {
                    Console.Write($"Select a top-level mod directory to use mod data [y/n]? ");
                    if (!promptYesNo())
                    {
                        Console.WriteLine();
                        break;
                    }
                }
                if (FileDialog.OpenFolderDialog(out string path))
                {
                    Console.WriteLine();
                    if (!Directory.Exists(path))
                    {
                        Console.WriteLine();
                        Console.WriteLine($"Error: Directory \"{path}\" not found");
                        continue;
                    }
                    {
                        if (path.EndsWith(@"\script\talk"))
                        {
                            string realPath = Path.GetFullPath(Path.Combine(path, @"..\.."));
                            Console.WriteLine($"You've selected an ESD directory, not the top-level mod directory.");
                            Console.Write($"Use \"{realPath}\" instead [y/n]? ");
                            if (promptYesNo())
                            {
                                path = realPath;
                            }
                            Console.WriteLine();
                        }
                        if (path == config.BaseDir)
                        {
                            Console.WriteLine($"Error: You selected the game directory. Select a separate mod directory.");
                            Console.WriteLine();
                            continue;
                        }
                        config.ModDir = path;
                    }
                }
            }
            if (promptDecompile)
            {
                while (config.Decompile.Count == 0)
                {
                    Console.WriteLine("Select one more esd or esdbnd files in the game directory to decompile.");
                    if (gameInfo.EsdDir != null) Console.WriteLine($"These are usually found in {gameInfo.EsdDir} after unpacking with UXM/UDSFM.");
                    Console.Write("Press enter to select files. ");
                    promptAny();
                    string gamePrefix = config.BaseDir + @"\";
                    if (FileDialog.OpenMultiFileDialog(Array.Empty<string>(), out IReadOnlyList<string> paths, config.BaseDir))
                    {
                        Console.WriteLine();
                        foreach (string path in paths)
                        {
                            string gamePath = Path.GetFullPath(path);
                            if (!gamePath.StartsWith(gamePrefix))
                            {
                                Console.WriteLine($"Ignoring \"{gamePath}\" because it's not in the game directory.");
                                continue;
                            }
                            string relPath = gamePath.Substring(gamePrefix.Length);
                            string modPath = Path.GetFullPath(Path.Combine(config.ModDir, relPath));
                            if (File.Exists(modPath))
                            {
                                Console.WriteLine($"Ignoring \"{gamePath}\" because it already exists in the mod directory.");
                                continue;
                            }
                            Console.WriteLine($"Copying \"{gamePath}\" to the mod directory");
                            Directory.CreateDirectory(Path.GetDirectoryName(modPath));
                            File.Copy(gamePath, modPath);
                            config.Decompile[gamePath] = modPath;
                            files.Add(modPath);
                        }
                        Console.WriteLine();
                    }
                }
            }

            if (configPath == null)
            {
                if (config.Decompile.Count > 0)
                {
                    inputFile = config.Decompile.Values.First();
                    string configDir = Path.GetDirectoryName(inputFile);
                    configPath = Path.Combine(configDir, "esdtoolconfig.json");
                    if (File.Exists(configPath))
                    {
                        // Merge the configs here.
                        // The user should really drag this config file instead, though.
                        OptionsConfig oldConfig = config;
                        config = ReadExistingConfig(configPath);
                        config.Game = oldConfig.Game;
                        config.BaseDir = oldConfig.BaseDir;
                        config.ModDir = oldConfig.ModDir;
                    }
                }
                else
                {
                    Console.WriteLine("Error: No input files given! Nothing to do...");
                    Console.WriteLine();
                    return null;
                }
            }

            string getPathToParent(string parentDir, string childDir)
            {
                parentDir = Path.GetFullPath(parentDir);
                childDir = Path.GetFullPath(childDir);
                if (childDir.StartsWith(parentDir))
                {
                    return Path.GetRelativePath(childDir, parentDir);
                }
                return parentDir;
            }
            if (!string.IsNullOrWhiteSpace(config.ModDir))
            {
                // Paths are currently relative to the esdtool.exe directory, TODO make them relative to the file directory
                // config.ModDir = getPathToParent(config.ModDir, Path.GetDirectoryName(configPath));
            }

            // This is not great because it duplicates esdbnds, but is still useful for py files.
            if (firstTimeRun)
            {
                Console.Write($"Create backups when overwriting files [y/n]? ");
                config.Backup = promptYesNo();
                Console.WriteLine();
            }

            Console.WriteLine($"Writing config {configPath}");
            Console.WriteLine();
            Console.WriteLine("Use the command line interface directly if you want to access exciting advanced functionality. You can also edit the config.");
            Console.WriteLine();
            // Add optional fields for documentation's sake
            config.ModDir ??= "";
            config.Options ??= "";
            config.ExtraESDs ??= new();
            File.WriteAllText(configPath, JsonConvert.SerializeObject(config, Formatting.Indented) + Environment.NewLine);
            return config;
        }

        public List<string> MakeOptions(IList<string> files)
        {
            List<string> ret = new List<string>();
            // Brain-dead options list, no validation
            // Aim for precision rather than massaging bad inputs
            if (!string.IsNullOrWhiteSpace(Game))
            {
                ret.Add($"-{Game}");
            }
            if (!string.IsNullOrWhiteSpace(BaseDir))
            {
                ret.Add($"-basedir");
                ret.Add(BaseDir);
            }
            if (!string.IsNullOrWhiteSpace(ModDir))
            {
                ret.Add($"-moddir");
                ret.Add(ModDir);
            }
            if (Backup)
            {
                ret.Add($"-backup");
            }
            if (ExtraESDs != null && ExtraESDs.Count > 0)
            {
                ret.Add($"-extra");
                foreach (KeyValuePair<string, string> entry in ExtraESDs)
                {
                    ret.Add($"{entry.Key}={entry.Value}");
                }
            }
            if (!string.IsNullOrWhiteSpace(Options))
            {
                ret.AddRange(SplitCommandLine(Options));
            }
            List<string> errors = new List<string>();
            // Check in advance if there are multiple bnd files to unpack, so we can do it in directory, which is the preferred workflow
            Dictionary<string, List<string>> bndsByDirectory = new Dictionary<string, List<string>>();
            foreach (string file in files)
            {
                if (File.Exists(file))
                {
                    FileInfo fileInfo = new FileInfo(file);
                    string name = fileInfo.Name;
                    string dir = fileInfo.DirectoryName;
                    if (name.EndsWith(".talkesdbnd") || name.EndsWith(".talkesdbnd.dcx"))
                    {
                        if (!bndsByDirectory.TryGetValue(dir, out List<string> names))
                        {
                            bndsByDirectory[dir] = names = new List<string>();
                        }
                        names.Add(fileInfo.FullName);
                    }
                }
            }
            Dictionary<string, string> directoryBndTargets = new Dictionary<string, string>();
            foreach (KeyValuePair<string, List<string>> entry in bndsByDirectory)
            {
                foreach (string bnd in entry.Value)
                {
                    Console.WriteLine(bnd);
                }
                Console.WriteLine();
                if (entry.Value.Count == 1)
                {
                    Console.WriteLine($"Note: ESD files from multiple different bnd files can all be decompiled to the same directory. When the directory is recompiled, it automatically updates all of the bnds containing those files.");
                    Console.WriteLine();
                    Console.WriteLine("Enter a directory name to enable editing multiple bnds, or else enter nothing to create a directory limited to only this bnd file.");
                }
                else
                {
                    Console.WriteLine($"You've selected multiple bnd files in the same directory. Decompiled files from different bnds can be added to a single directory. When the directory is recompiled, it updates all of the bnds containing those files.");
                    Console.WriteLine();
                    Console.WriteLine("Enter a directory name for all decompiled files, or else enter nothing to create separate directories limited to only their bnd files.");
                }
                Console.WriteLine();
                while (true)
                {
                    Console.Write("Shared directory name for all ESDs, or else nothing: ");
                    string text = Console.ReadLine();
                    if (text == null) return null;
                    text = text.Trim();
                    if (string.IsNullOrWhiteSpace(text))
                    {
                        break;
                    }
                    if (text.IndexOfAny(Path.GetInvalidFileNameChars()) < 0)
                    {
                        directoryBndTargets[entry.Key] = text;
                        break;
                    }
                    else
                    {
                        Console.WriteLine($"Invalid directory name");
                        Console.WriteLine();
                    }
                }
            }
            Console.WriteLine();
            Dictionary<(string, string), List<string>> inputsByOutput = new Dictionary<(string, string), List<string>>();
            void addInput(string operation, string input, string output)
            {
                (string, string) key = (operation, output);
                if (!inputsByOutput.TryGetValue(key, out List<string> inputs))
                {
                    inputsByOutput[key] = inputs = new List<string>();
                }
                inputsByOutput[key].Add(input);
            }
            foreach (string file in files)
            {
                // Don't validate these file paths too hard, as they should come from drag-and-drop
                if (Directory.Exists(file))
                {
                    DirectoryInfo dirInfo = new DirectoryInfo(file);
                    List<string> pys = Directory.GetFiles(dirInfo.FullName, "*.py").ToList();
                    string parent = dirInfo.Parent.FullName;
                    if (dirInfo.Name.EndsWith("-only"))
                    {
                        string prefix = dirInfo.Name.Substring(0, dirInfo.Name.LastIndexOf("-only"));
                        string pattern = $"{prefix}.*esdbnd";
                        List<string> match = Directory.GetFiles(parent, pattern).Concat(Directory.GetFiles(parent, pattern + ".dcx")).ToList();
                        if (match.Count == 0)
                        {
                            errors.Add($"Can't pack {dirInfo.FullName}: No ESD files for {prefix} found in {dirInfo.Parent.Name} directory");
                        }
                        else if (match.Count > 1)
                        {
                            errors.Add($"Can't pack {dirInfo.FullName}: Multiple ESD files matching {prefix} found in {dirInfo.Parent.Name} directory");
                        }
                        else
                        {
                            foreach (string py in pys)
                            {
                                addInput("writebndfile", py, match[0]);
                            }
                        }
                    }
                    else
                    {
                        if (Directory.GetFiles(parent, "*esdbnd.dcx").Count() == 0 && Directory.GetFiles(parent, "*esdbnd").Count() == 0)
                        {
                            // This is fine actually
                            // errors.Add($"Can't pack {dirInfo.FullName}: no ESD BND files found in {dirInfo.Parent.Name} directory");
                        }
                        foreach (string py in pys)
                        {
                            addInput("writebnd", py, parent);
                        }
                    }
                }
                else if (File.Exists(file))
                {
                    FileInfo fileInfo = new FileInfo(file);
                    string name = fileInfo.Name;
                    if (name.EndsWith(".py"))
                    {
                        addInput("writeloose", fileInfo.FullName, Path.Combine(fileInfo.DirectoryName, "%e.esd"));
                    }
                    else if (name.EndsWith(".esd") || name.EndsWith(".esd.dcx"))
                    {
                        addInput("writepy", fileInfo.FullName, Path.Combine(fileInfo.DirectoryName, "%e.py"));
                    }
                    else if (name.EndsWith(".talkesdbnd") || name.EndsWith(".talkesdbnd.dcx"))
                    {
                        if (!directoryBndTargets.TryGetValue(fileInfo.DirectoryName, out string relDirName))
                        {
                            relDirName = name.Substring(0, name.LastIndexOf(".talkesdbnd")) + "-only";
                        }
                        addInput("writepy", fileInfo.FullName, Path.Combine(Path.Combine(fileInfo.DirectoryName, relDirName), "%e.py"));
                    }
                    else
                    {
                        errors.Add($"{file} is not named like an Python file, ESD, or talk ESD BND");
                    }
                }
                else
                {
                    errors.Add($"{file} not found");
                }
            }
            foreach (KeyValuePair<(string, string), List<string>> entry in inputsByOutput)
            {
                (string operation, string output) = entry.Key;
                ret.Add("-i");
                ret.AddRange(entry.Value);
                ret.Add("-" + operation);
                ret.Add(output);
            }
            if (errors.Count > 0)
            {
                Console.WriteLine("Error: Unrecognized files:");
                foreach (string error in errors) Console.WriteLine(error);
                Console.WriteLine();
                return null;
            }
            return ret;
        }

        private static List<string> SplitCommandLine(string str)
        {
            // This sure would be great functionality to have in a language's standard library
            List<string> args = new List<string>();
            StringBuilder sb = new StringBuilder();
            char? quoteCh = null;
            foreach (char ch in str)
            {
                // Basic paired quote marks. Don't try to handle escaping
                if (ch == '"' || ch == '\'')
                {
                    if (quoteCh is char prevCh && ch == prevCh)
                    {
                        quoteCh = null;
                    }
                    else if (quoteCh is null)
                    {
                        quoteCh = ch;
                    }
                }
                if (quoteCh is null && ch == ' ')
                {
                    if (sb.Length > 0)
                    {
                        args.Add(sb.ToString());
                        sb.Clear();
                    }
                }
                else
                {
                    sb.Append(ch);
                }
            }
            if (sb.Length > 0)
            {
                args.Add(sb.ToString());
            }
            string unquote(string text)
            {
                if (text.Length >= 2 && (text[0] == '"' || text[0] == '\'') && text[0] == text[text.Length - 1])
                {
                    return text.Substring(1, text.Length - 2);
                }
                return text;
            }
            return args.Select(unquote).ToList();
        }
    }
}
