using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.RegularExpressions;

namespace ESDLang.Doc
{
    /// <summary>
    /// JSON-serializable documentation for a type of ESD.
    /// 
    /// All names should be camelcase and usable as identifiers in most programming languages, matching [A-Za-z0-9_]+
    /// Method and enum names should be uppercase.
    /// </summary>
    public class ESDDocumentation
    {
        /// <summary>
        /// Required. All commands in all games, without any filters.
        /// </summary>
        [JsonPropertyName("commands")]
        public List<MethodDoc> CommandList { get; set; }
        /// <summary>
        /// Required. All functions in all games, without any filters.
        /// </summary>
        [JsonPropertyName("functions")]
        public List<MethodDoc> FunctionList { get; set; }
        /// <summary>
        /// Required. All enums in all games, without any filters.
        /// </summary>
        [JsonPropertyName("enums")]
        public List<EnumDoc> EnumList { get; set; }
        /// <summary>
        /// Required. The argument to automatically add to bank 5 commands, if enabled by options.
        /// </summary>
        [JsonPropertyName("condition_arg")]
        public ArgDoc ConditionArg { get; set; }

        public static readonly HashSet<string> ValidArgTypes = new() { "int", "float", "double", "string", "bool", "enum" };

        public class DocOptions
        {
            /// <summary>
            /// Whether to validate and process the config. If turned off, this will only parse the JSON and not populate any indices.
            /// </summary>
            public bool Process { get; set; } = true;

            /// <summary>
            /// The game to process commands for, which will apply filters during processing. See MethodDoc.Games for recognized names.
            /// 
            /// If not given, this will use the default definitions for a given id, if any exist.
            /// </summary>
            public string Game { get; set; }

            /// <summary>
            /// Whether to add conditional versions of commands automatically, if the game is known to support it.
            /// </summary>
            public bool AddConditionalCommands { get; set; } = true;
        }

        // These are filled in when processing is enabled in options.
        [JsonIgnore]
        public Dictionary<(int, int), MethodDoc> Commands { get; set; }
        [JsonIgnore]
        public Dictionary<int, MethodDoc> Functions { get; set; }
        // Mappings by name may contain deprecated names. Check the doc itself for the current authoritative name.
        [JsonIgnore]
        public Dictionary<string, MethodDoc> CommandsByName { get; set; }
        [JsonIgnore]
        public Dictionary<string, MethodDoc> FunctionsByName { get; set; }
        [JsonIgnore]
        public Dictionary<string, EnumDoc> Enums { get; set; }

        private static readonly JsonSerializerOptions jsonOptions = new()
        {
            WriteIndented = true,
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingDefault,
        };

        public string SerializeToText()
        {
            string text = JsonSerializer.Serialize(this, jsonOptions);
            // Formatting customization is abyssmal for this bloated overengineered JSON library so regex it is.
            Regex simpleStringList = new Regex(@"\[\s*(""\w+"")(?:\s*,\s*(""\w+"")\s*)*\s*\]");
            text = simpleStringList.Replace(text, match =>
            {
                List<string> strs = new() { match.Groups[1].Value };
                strs.AddRange(match.Groups[2].Captures.Select(c => c.Value));
                return "[" + string.Join(", ", strs) + "]";
            });
            Regex entryRegex = new Regex(@"{\s*""value"": (\w+),\s*""name"": (""\w+"")(?:,\s*""deprecated"": (\w+))?\s*}");
            text = entryRegex.Replace(text, match =>
            {
                string val = @$"""value"": {match.Groups[1].Value}, ""name"": {match.Groups[2].Value}";
                if (match.Groups[3].Success)
                {
                    val += @$", ""deprecated"": {match.Groups[3].Value}";
                }
                return "{" + val + "}";
            });
            return text;
        }

        public static ESDDocumentation DeserializeFromFile(string file, DocOptions opt)
        {
            ESDDocumentation doc;
            using (var reader = File.OpenRead(file))
            {
                doc = JsonSerializer.Deserialize<ESDDocumentation>(reader, jsonOptions);
            }
            doc.Process(opt);
            return doc;
        }

        public static ESDDocumentation DeserializeFromText(string text, DocOptions opt)
        {
            ESDDocumentation doc = JsonSerializer.Deserialize<ESDDocumentation>(text, jsonOptions);
            doc.Process(opt);
            return doc;
        }

        public bool TryGetEnumValue(string enumName, string fieldName, out int value)
        {
            value = 0;
            return Enums.TryGetValue(enumName, out EnumDoc enumDoc) && enumDoc.Values.TryGetValue(fieldName, out value);
        }

        public string GetEnumString(string enumName, int value)
        {
            if (Enums.TryGetValue(enumName, out EnumDoc enumDoc) && enumDoc.Names.TryGetValue(value, out string fieldName))
            {
                return $"{enumName}.{fieldName}";
            }
            return value.ToString();
        }

        /// <summary>
        /// Documentation for a function or command.
        /// </summary>
        public class MethodDoc
        {
            /// <summary>
            /// For commands, the bank. Automatically filled in if processing is enabled.
            /// </summary>
            [JsonPropertyName("bank")]
            public int Bank { get; set; }

            /// <summary>
            /// Required. For functions, the id. For commands, the id in bank 1.
            /// 
            /// Bank 5 uses the same attributes except "If" added at the end of the name, and a bool condition is added as the
            /// first argument. This is done automatically by the game, so there's no reason to have manual entries for them.
            /// 
            /// Banks 6 and 7 are out of scope of docs and should be handled by each editor.
            /// </summary>
            [JsonIgnore(Condition = JsonIgnoreCondition.Never)]
            [JsonPropertyName("id")]
            public int ID { get; set; } = -1;

            [JsonIgnore]
            public string MethodID => Bank == 0 ? $"f{ID}" : $"c{Bank}_{ID}";

            /// <summary>
            /// Optional. If missing, a placeholder can be used, like c1_130 for commands or f50 for functions.
            /// </summary>
            [JsonPropertyName("name")]
            public string Name { get; set; }

            /// <summary>
            /// Optional. Contains previously used names for backwards compatibility, not to be used in decompilation.
            /// </summary>
            [JsonPropertyName("deprecated_names")]
            public List<string> DeprecatedNames { get; set; }

            /// <summary>
            /// Optional, for when methods are incompatible between games.
            /// 
            /// This uses game IDs from SoulsIds: des, ds1, ds1r, ds2, ds2s, bb, ds3, sdt, er, ac6
            /// 
            /// If this is specified for one command id, it must be specified for all of them, and must be mutually exclusive.
            /// When processing the config for a specific game, duplicates are not allowed.
            /// </summary>
            [JsonPropertyName("games")]
            public List<string> Games { get; set; }

            /// <summary>
            /// Optional. Contains all games where this command is used, for documentation purposes.
            /// 
            /// Editors can ignore or deprioritize methods which are not used by certain games.
            /// </summary>
            [JsonPropertyName("games_used")]
            public List<string> GamesUsed { get; set; }

            /// <summary>
            /// Optional. Provides information about the method that script-writers can use.
            /// </summary>
            [JsonPropertyName("comment")]
            public string Comment { get; set; }

            /// <summary>
            /// Optional. Has known args for this method.
            /// </summary>
            [JsonPropertyName("args")]
            public List<ArgDoc> Args { get; set; }

            /// <summary>
            /// Optional. Contains return type info for functions which can be used by some editors.
            /// </summary>
            [JsonPropertyName("return_value")]
            public ArgDoc ReturnValue { get; set; }

            /// <summary>
            /// Optional. Determines whether it's safe to remove func()==1 conditions for function return results.
            /// 
            /// This is distinct from just having a bool return type, as some methods like CompareRNGValue normally
            /// return a bool but can also return -1 to indicate RNG is not initialized. Also, this can apply to non-bool
            /// enums. As such, this should require very high certainty to set, by reverse engineering the function itself.
            /// 
            /// Note it is safe to negate func()==0 conditions, because in that case all non-0 values are treated the same.
            /// </summary>
            [JsonPropertyName("binary_return")]
            public bool BinaryReturn { get; set; }

            public MethodDoc Clone()
            {
                MethodDoc o = (MethodDoc)MemberwiseClone();
                o.DeprecatedNames = o.DeprecatedNames?.ToList();
                o.Games = o.Games?.ToList();
                o.GamesUsed = o.GamesUsed?.ToList();
                o.Args = o.Args?.Select(x => x.Clone()).ToList();
                o.ReturnValue = o.ReturnValue?.Clone();
                return o;
            }
        }

        /// <summary>
        /// Documentation for an argument for a function or command.
        /// </summary>
        public class ArgDoc
        {
            /// <summary>
            /// Optional.
            /// </summary>
            [JsonPropertyName("name")]
            public string Name { get; set; }

            /// <summary>
            /// Optional. Valid types are int, float, double, string, bool, enum.
            /// Types bool and enum are both int, but special-cased for documentation convenience.
            /// 
            /// Most of these are interchangeable at runtime, like ints and floats, depending on the interpreter's implementation.
            /// 
            /// Unsigned values are not known to be supported.
            /// </summary>
            [JsonPropertyName("type")]
            public string Type { get; set; }

            /// <summary>
            /// Required if Type is enum. This must point to a valid enum name.
            /// 
            /// It is permitted if enum values are defined for some games and not others, and an empty enum will
            /// automatically be created in the latter case.
            /// </summary>
            [JsonPropertyName("enum")]
            public string EnumName { get; set; }

            /// <summary>
            /// For convenience, a reference to the enum corresponding to EnumName, added when processed.
            /// </summary>
            [JsonIgnore]
            public EnumDoc Enum { get; set; }

            /// <summary>
            /// True if the game will accept this method with this argument missing.
            /// 
            /// This should only be set for args which are last in the list.
            /// </summary>
            [JsonPropertyName("optional")]
            public bool Optional { get; set; }

            /// <summary>
            /// Optional. This is the type of reference for the object for metadata purposes.
            /// 
            /// In ESDLang, this matches Universe.Namespace. This can be standardized,
            /// or alternatively different extensions can be used by different editors.
            /// </summary>
            [JsonPropertyName("namespace")]
            public string Namespace { get; set; }

            /// <summary>
            /// Optional. Provides information about the method that script-writers can use.
            /// </summary>
            [JsonPropertyName("comment")]
            public string Comment { get; set; }

            public ArgDoc Clone() => (ArgDoc)MemberwiseClone();
        }

        /// <summary>
        /// Documentation for an enum entry. These are turned into maps in EnumDoc when processing is enabled.
        /// </summary>
        public class EnumEntryDoc
        {
            /// <summary>
            /// Required. Integer value of the enum. Each value must have at most one non-deprecated entry.
            /// </summary>
            [JsonIgnore(Condition = JsonIgnoreCondition.Never)]
            [JsonPropertyName("value")]
            public int Value { get; set; }

            /// <summary>
            /// Required. Name for the enum value.
            /// </summary>
            [JsonPropertyName("name")]
            public string Name { get; set; }

            /// <summary>
            /// Optional. Name for backwards compatibility, not to be used in decompilation.
            /// </summary>
            [JsonPropertyName("deprecated")]
            public bool Deprecated { get; set; }

            public EnumEntryDoc Clone() => (EnumEntryDoc)MemberwiseClone();
        }

        /// <summary>
        /// Documentation for an enum.
        /// </summary>
        public class EnumDoc
        {
            /// <summary>
            /// Required. Name of the enum.
            /// </summary>
            [JsonPropertyName("name")]
            public string Name { get; set; }

            /// <summary>
            /// Optional. Contains previously used names for backwards compatibility, not to be used in decompilation.
            /// </summary>
            [JsonPropertyName("deprecated_names")]
            public List<string> DeprecatedNames { get; set; }

            /// <summary>
            /// Optional, for when enums are incompatible between games. See MethodDoc as this works the same way.
            /// 
            /// If there is no matching enum for a game, it's given a blank enum so that methods can reference it.
            /// </summary>
            [JsonPropertyName("games")]
            public List<string> Games { get; set; }

            /// <summary>
            /// Required.
            /// </summary>
            [JsonPropertyName("entries")]
            public List<EnumEntryDoc> Entries { get; set; }

            /// <summary>
            /// Mapping from enum values to the authoritative name, only present if processed.
            /// </summary>
            [JsonIgnore]
            public Dictionary<int, string> Names { get; set; }

            /// <summary>
            /// Mapping from enum names to the value, including deprecated names, only present if processed.
            /// </summary>
            [JsonIgnore]
            public Dictionary<string, int> Values { get; set; }

            public EnumDoc Clone()
            {
                EnumDoc o = (EnumDoc)MemberwiseClone();
                o.Entries = o.Entries.Select(x => x.Clone()).ToList();
                o.DeprecatedNames = o.DeprecatedNames?.ToList();
                return o;
            }
        }

        public void Process(DocOptions opt)
        {
            if (!opt.Process)
            {
                if (Commands != null)
                {
                    // If reprocessing, clear everything out which may become invalid between games.
                    Commands = null;
                    Functions = null;
                    CommandsByName = null;
                    FunctionsByName = null;
                    Enums = null;
                    foreach (MethodDoc methodDoc in CommandList.Concat(FunctionList))
                    {
                        foreach (ArgDoc argDoc in methodDoc.Args ?? new())
                        {
                            argDoc.Enum = null;
                        }
                    }
                }
                return;
            }
            if (CommandList == null || FunctionList == null || ConditionArg == null || EnumList == null)
            {
                throw new ArgumentException("Config error: missing required fields");
            }
            bool gameApplies(List<string> games)
            {
                return opt.Game == null || games == null || games.Contains(opt.Game);
            }
            Enums = new();
            HashSet<string> allEnumNames = new();
            foreach (EnumDoc enumDoc in EnumList)
            {
                if (enumDoc.Name == null || enumDoc.Entries == null)
                {
                    throw new ArgumentException($"Config error: missing fields in enum {enumDoc.Name}");
                }
                allEnumNames.Add(enumDoc.Name);
                if (!gameApplies(enumDoc.Games))
                {
                    continue;
                }
                List<string> names = new() { enumDoc.Name };
                if (enumDoc.DeprecatedNames != null)
                {
                    names.AddRange(enumDoc.DeprecatedNames);
                }
                foreach (string name in names)
                {
                    if (opt.Game != null && Enums.ContainsKey(name))
                    {
                        throw new ArgumentException($"Config error: duplicate enum name {name} for game {opt.Game}");
                    }
                    Enums[name] = enumDoc;
                }
                enumDoc.Names = new();
                enumDoc.Values = new();
                foreach (EnumEntryDoc entryDoc in enumDoc.Entries)
                {
                    if (entryDoc.Name == null)
                    {
                        throw new ArgumentException($"Config error: missing enum entry name in {enumDoc.Name} value {entryDoc.Value}");
                    }
                    if (enumDoc.Values.TryGetValue(entryDoc.Name, out int otherValue))
                    {
                        // Require disambiguating multiple names in the config itself, even if it's just adding numbers at the end
                        throw new ArgumentException($"Config error: duplicate enum name {enumDoc.Name}.{entryDoc.Name} for values {otherValue} and {entryDoc.Value}");
                    }
                    enumDoc.Values[entryDoc.Name] = entryDoc.Value;
                    if (!entryDoc.Deprecated)
                    {
                        if (enumDoc.Names.TryGetValue(entryDoc.Value, out string otherName))
                        {
                            throw new ArgumentException($"Config error: duplicate enum value {entryDoc.Value} for names {enumDoc.Name}.{otherName} and {enumDoc.Name}.{entryDoc.Name}");
                        }
                        enumDoc.Names[entryDoc.Value] = entryDoc.Name;
                    }
                }
            }
            // Do DS1, DS1R, BB support this? It's unused there.
            bool addCond = opt.AddConditionalCommands && opt.Game != "des";
            Commands = new();
            foreach (MethodDoc methodDoc in CommandList)
            {
                if (methodDoc.ID == -1)
                {
                    throw new ArgumentException($"Config error: no ID for command {methodDoc.Name}");
                }
                if (!gameApplies(methodDoc.Games))
                {
                    continue;
                }
                methodDoc.Bank = 1;
                if (opt.Game != null && Commands.ContainsKey((1, methodDoc.ID)))
                {
                    throw new ArgumentException($"Config error: {methodDoc.MethodID} defined multiple times for game {opt.Game}");
                }
                Commands[(1, methodDoc.ID)] = methodDoc;
                if (addCond)
                {
                    MethodDoc condDoc = methodDoc.Clone();
                    condDoc.Bank = 5;
                    if (condDoc.Name != null)
                    {
                        condDoc.Name = $"{condDoc.Name}If";
                    }
                    if (condDoc.DeprecatedNames != null)
                    {
                        condDoc.DeprecatedNames = condDoc.DeprecatedNames.Select(n => $"{n}If").ToList();
                    }
                    // If no args are documented, this will at least include the one certain arg.
                    condDoc.Args ??= new();
                    condDoc.Args.Insert(0, ConditionArg);
                    Commands[(5, methodDoc.ID)] = condDoc;
                }
            }
            CommandsByName = new();
            foreach (MethodDoc methodDoc in Commands.Values)
            {
                List<string> names = new();
                if (methodDoc.Name != null)
                {
                    names.Add(methodDoc.Name);
                }
                if (methodDoc.DeprecatedNames != null)
                {
                    names.AddRange(methodDoc.DeprecatedNames);
                }
                foreach (string name in names)
                {
                    if (CommandsByName.TryGetValue(name, out MethodDoc otherDoc))
                    {
                        throw new ArgumentException($"Config error: duplicate command name {name} applies to both {methodDoc.MethodID} and {otherDoc.MethodID}");
                    }
                    CommandsByName[name] = methodDoc;
                }
                if (methodDoc.ReturnValue != null)
                {
                    throw new ArgumentException($"Config error: command {methodDoc.MethodID} must not have return value");
                }
            }
            Functions = new();
            foreach (MethodDoc methodDoc in FunctionList)
            {
                if (methodDoc.ID == -1)
                {
                    throw new ArgumentException($"Config error: no ID for function {methodDoc.Name}");
                }
                if (!gameApplies(methodDoc.Games))
                {
                    continue;
                }
                if (opt.Game != null && Functions.ContainsKey(methodDoc.ID))
                {
                    throw new ArgumentException($"Config error: {methodDoc.MethodID} defined multiple times for game {opt.Game}");
                }
                Functions[methodDoc.ID] = methodDoc;
            }
            FunctionsByName = new();
            foreach (MethodDoc methodDoc in Functions.Values)
            {
                List<string> names = new();
                if (methodDoc.Name != null)
                {
                    names.Add(methodDoc.Name);
                }
                if (methodDoc.DeprecatedNames != null)
                {
                    names.AddRange(methodDoc.DeprecatedNames);
                }
                foreach (string name in names)
                {
                    if (FunctionsByName.TryGetValue(name, out MethodDoc otherDoc))
                    {
                        throw new ArgumentException($"Config error: duplicate function name {name} applies to both {methodDoc.MethodID} and {otherDoc.MethodID}");
                    }
                    if (CommandsByName.TryGetValue(name, out MethodDoc cmdDoc))
                    {
                        // Also check functions and commands don't share names, for compatibility with possible scripting implementations.
                        // This is not the case in DS2 as of late 2024, as functions and condition commands shared names and
                        // sometimes both are used, e.g. IsOffline. These may get renamed in the future.
                        if (opt.Game == null || !opt.Game.StartsWith("ds2"))
                        {
                            throw new ArgumentException($"Config error: {name} applies to both {methodDoc.MethodID} and {cmdDoc.MethodID}");
                        }
                    }
                    FunctionsByName[name] = methodDoc;
                }
            }
            // Validate all args at once
            foreach (MethodDoc methodDoc in Commands.Values.Concat(Functions.Values))
            {
                List<ArgDoc> args = new List<ArgDoc>();
                if (methodDoc.ReturnValue != null)
                {
                    args.Add(methodDoc.ReturnValue);
                    if (methodDoc.ReturnValue.Optional)
                    {
                        // For tracking below
                        throw new ArgumentException($"Config error: return value cannot be optional in {methodDoc.MethodID}");
                    }
                }
                if (methodDoc.Args != null)
                {
                    args.AddRange(methodDoc.Args);
                }
                bool anyOptional = false;
                foreach (ArgDoc argDoc in args)
                {
                    if (argDoc.Type != null)
                    {
                        if (!ValidArgTypes.Contains(argDoc.Type))
                        {
                            throw new ArgumentException($"Config error: invalid argument type {argDoc.Type} in {methodDoc.MethodID}");
                        }
                        if (argDoc.Type == "enum")
                        {
                            if (argDoc.EnumName == null)
                            {
                                throw new ArgumentException($"Config error: enum argument in {methodDoc.MethodID} is missing its enum name");
                            }
                            if (Enums.TryGetValue(argDoc.EnumName, out EnumDoc enumDoc))
                            {
                                argDoc.Enum = enumDoc;
                            }
                            else if (allEnumNames.Contains(argDoc.EnumName))
                            {
                                // As a convenience, make a fake enum so that methods can be used in games where this enum is not yet documented.
                                // This could also be done during enum processing.
                                Enums[argDoc.EnumName] = argDoc.Enum = new EnumDoc
                                {
                                    Name = argDoc.EnumName,
                                    Entries = new(),
                                    Names = new(),
                                    Values = new(),
                                };
                            }
                            else
                            {
                                throw new ArgumentException($"Config error: enum argument in {methodDoc.MethodID} has unknown enum type {argDoc.EnumName}");
                            }
                        }
                        else if (argDoc.EnumName != null)
                        {
                            throw new ArgumentException($"Config error: non-enum argument in {methodDoc.MethodID} has enum type {argDoc.EnumName}");
                        }
                    }
                    if (anyOptional && !argDoc.Optional)
                    {
                        throw new ArgumentException($"Config error: optional parameters must be in final positions in {methodDoc.MethodID}");
                    }
                    anyOptional |= argDoc.Optional;
                }
            }
        }
    }
}
