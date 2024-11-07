using Newtonsoft.Json;
using Org.BouncyCastle.Asn1.Cms;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using static SoulsIds.GameSpec;

namespace ESDLang.Script
{
    // Extremely limited readonly copy of DSMapStudio/Smithbox ProjectSettings just to extract project data.
    // Based on DarkScript3 but instead of event directory logic, has esd directory logic.
    // This is somewhat redundant to GameSpec.
    public class ProjectSettingsFile
    {
        // Project file contents
        public ProjectSettings Settings { get; set; }
        // Project file path, which exists
        public string FilePath { get; set; }
        // Main mod directory based on FilePath
        public string ModDir => Path.GetDirectoryName(FilePath);
        // Supported ESDLang game, if any
        public FromGame Game { get; set; } = FromGame.UNKNOWN;
        // Game directory, if it exists
        public string GameDir { get; set; }

        // https://github.com/soulsmods/DSMapStudio/blob/master/StudioCore/GameType.cs
        // https://github.com/vawser/Smithbox/blob/main/src/StudioCore/Core/Project/ProjectType.cs
        public enum GameType
        {
            Undefined = 0,
            // DSMS names
            DemonsSouls = 1,
            DarkSoulsPTDE = 2,
            DarkSoulsRemastered = 3,
            DarkSoulsIISOTFS = 4,
            DarkSoulsIII = 5,
            Bloodborne = 6,
            Sekiro = 7,
            EldenRing = 8,
            // Smithbox names
            // Duplicates is fine but makes reflection name lookup ambiguous
            DES = 1,
            DS1 = 2,
            DS1R = 3,
            DS2S = 4,
            DS3 = 5,
            BB = 6,
            SDT = 7,
            ER = 8,
            AC6 = 9,
            DS2 = 10,
            AC4 = 11,
            ACFA = 12,
            ACV = 13,
            ACVD = 14,
        }

        // https://github.com/soulsmods/DSMapStudio/blob/master/StudioCore/Editor/ProjectSettings.cs
        // https://github.com/vawser/Smithbox/blob/main/src/StudioCore/Core/Project/ProjectConfiguration.cs
        public class ProjectSettings
        {
            public string ProjectName { get; set; } = "";
            public string GameRoot { get; set; } = "";
            public GameType GameType { get; set; } = GameType.Undefined;
        }

        private static readonly List<string> knownRelativeDirs = new()
        {
            "script\\talk", "chr", "ezstate",
        };
        private static readonly Dictionary<GameType, FromGame> supportedGames = new()
        {
            // For now, all of the names match with the Smithbox version
            [GameType.DES] = FromGame.DES,
            [GameType.DS1] = FromGame.DS1,
            [GameType.DS1R] = FromGame.DS1R,
            [GameType.BB] = FromGame.BB,
            [GameType.DS2] = FromGame.DS2,
            [GameType.DS2S] = FromGame.DS2S,
            [GameType.DS3] = FromGame.DS3,
            [GameType.SDT] = FromGame.SDT,
            [GameType.ER] = FromGame.ER,
            [GameType.AC6] = FromGame.AC6,
        };

        // Expects a fully specified valid project JSON path.
        // This may throw an exception.
        public static ProjectSettingsFile LoadProjectFile(string projectJsonPath)
        {
            // Wrapper to rewrite exceptions
            try
            {
                return LoadProject(projectJsonPath);
            }
            catch (JsonException je)
            {
                throw new IOException($"Failed to parse {projectJsonPath}", je);
            }
            catch (IOException ie)
            {
                throw new IOException($"Failed to load {projectJsonPath}", ie);
            }
        }

        public static bool TryGetProjectFile(string inputPath, out string projectPath)
        {
            DirectoryInfo esdDir = Directory.Exists(inputPath) ? new DirectoryInfo(inputPath) : new FileInfo(inputPath).Directory;
            DirectoryInfo projectDir = esdDir;
            while (true)
            {
                projectPath = Path.Combine(projectDir.FullName, "project.json");
                if (File.Exists(projectPath))
                {
                    return true;
                }
                if (projectDir.Parent == null)
                {
                    projectPath = null;
                    return false;
                }
                projectDir = projectDir.Parent;
            }
        }

        private static ProjectSettingsFile LoadProject(string jsonPath)
        {
            jsonPath = Path.GetFullPath(jsonPath);
            string input = File.ReadAllText(jsonPath);
            ProjectSettings settings = JsonConvert.DeserializeObject<ProjectSettings>(input);
            ProjectSettingsFile file = new ProjectSettingsFile
            {
                Settings = settings,
                FilePath = jsonPath,
            };
            if (supportedGames.TryGetValue(settings.GameType, out FromGame game))
            {
                file.Game = game;
            }
            if (settings.GameRoot != null && Directory.Exists(settings.GameRoot))
            {
                file.GameDir = Path.GetFullPath(settings.GameRoot);
            }
            return file;
        }
    }
}
