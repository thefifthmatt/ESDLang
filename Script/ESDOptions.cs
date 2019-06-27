using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.IO;
using System.Threading.Tasks;
using SoulsFormats;
using SoulsIds;
using static SoulsIds.GameSpec;

namespace ESDLang.Script
{
    public class ESDOptions
    {
        // Options to process
        public /* . */ Queue<Option> opts = new Queue<Option>();
        // State
        public Dictionary<string, bool> Flags = new Dictionary<string, bool>();
        // For now, all flags are default true
        public bool Flag(string name) => Flags.TryGetValue(name, out bool val) ? val : true;
        public List<string> Chrs = new List<string>();
        public List<string> Maps = new List<string>();
        public List<string> Esds = new List<string>();
        public List<string> PyInputs = new List<string>();
        public List<string> EsdInputs = new List<string>();
        public GameSpec Spec = new GameSpec();
        public Option LastAction = null;

        private static readonly HashSet<string> yesFlags = new HashSet<string> { "cfg", "stateinfo", "newstates", "talk" };
        private static readonly HashSet<string> allFlags = new HashSet<string>(yesFlags.Concat(yesFlags.Select(f => $"no{f}")));
        private static readonly List<FromGame> gamesList = ((FromGame[])Enum.GetValues(typeof(FromGame))).Where(g => g != FromGame.UNKNOWN).ToList();
        private static readonly Dictionary<string, FromGame> games = gamesList.ToDictionary(f => f.ToString().ToLower(), f => f);
        private static readonly List<DCX.Type> dcxsList = ((DCX.Type[])Enum.GetValues(typeof(DCX.Type))).Where(d => d != DCX.Type.Unknown).ToList();
        private static readonly Dictionary<string, DCX.Type> dcxs = dcxsList.ToDictionary(f => f.ToString().ToLower(), f => f);
        public static readonly HashSet<string> specFlags = new HashSet<string> { "basedir", "esddir", "maps", "msgs", "names", "layouts", "params", "outdcx" };

        private ESDOptions(List<Option> opts)
        {
            this.opts = new Queue<Option>(opts);
        }
        public static string GetShortUsage()
        {
            return $@"Usage: esdtool.exe [-h] [{string.Join(" | ", gamesList.Select(g => $"-{g}".ToLower()))}]
                   [-basedir DIR] [-esddir DIR] [-maps DIR] [-msgs DIR] [-params FILE] [-names DIR]
                   [-layouts DIR] [-outdcx DCXTYPE] [-i FILE1 FILE2 etc] [-f ESD MAP CHR etc]
                   [-writepy TEMPLATE] [-writebnd DIR] [-writeloose TEMPLATE]
                   [-[no]cfg] [-[no]stateinfo] [-[no]newstates] [-[no]talk]
";
        }
        public static string GetUsage()
        {
            return $@"Usage: esdtool.exe <args>

esdtool decompiles ESDs to a high-level Python representation, which can be compiled back to ESD.
Similar to ffmpeg or ImageMagick, the order of command line arguments determines the order of
operations. For instance, -ds3 -esddir mod\script\talk will default everything to DS3, but then
change the subdirectory used for ESDs. The other way around will end up with the DS3 default
directory for ESDs only.

> Game flag
{string.Join(", ", gamesList.Select(g => $"-{g}".ToLower()))}
    Sets all game data flags to default known values for Steam installations of the given game, or
    clears them if unknown. This overrides all values which were there before. Note: esddir is
    currently only set for DS1R, DS3, and SDT. Contact me to add support for other games.

> Game data flags
(not necessary to set if set by the game flag)
-basedir DIR
    Sets the base directory for esddir, maps, msgs, and params. UXM or similar tool must be used.
-esddir DIR
    Sets the relative dir for all ESDs, meaning all .esd, .esd.dcx, and .esdbnd.dcx files in
    that directory. Overrides -i for a list of ESDs and clears -f.
-maps DIR
    Sets the relative dir for all MSB files. Used to look up chr info on ESDs, currently for
    Sekiro only.
-msgs DIR
    Sets the relative dir where FMG bnds can be found. Used to annotate ESDs with game info.
-params FILE
    Sets the relative file with game params. Used to annotate ESDs with game info.
    Requires -layouts.
-names DIR
    A directory with names for game ids. Currently ModelName.txt is used alongside chr info.
-layouts DIR
    A directory with layout xml files, required to use -params.
-outdcx [{string.Join(" | ", dcxsList)}]
    Sets the DCX type to use when writing ESDs (writebnd/writeloose).

> Input/output flags
-i FILE1 FILE2 etc
    Can be used in two ways, for a list of one or more files. If all files end in .py, sets
    the list of Python files to compile. If all files end in .esd, .esd.dcx, and .esdbnd.dcx,
    sets the list of ESD files to decompile; also overrides -esddir and clears -f. These are
    relative to the current directory if relative paths.
-f ESD MAP CHR etc
    A list of one or more filters for -esddir or -i inputs, replacing previous list of filters
    (if any). ESD is an ESD name (like t300330), MAP is a prefix for a BND name (like m40_00),
    and CHR is a character model with an ESD (like c1400, if -maps is supported). The ESDs
    output/replaced are a union of all filters. Filters do nothing if no input ESD matches them.
    Note that chresdbnd are already prefixed with the map name.
-writepy TEMPLATE
    Given ESD inputs (with -esddir or -i), decompile all ESDs, with filters if those exist. The
    template is a file name, with %e, %m, and %c replaced with ESD, map name prefix, and chr name
    respectively (if -maps is supported). First chr is used if there are multiple, and 'unk' if
    there are none. All ESDs matching the pattern while be combined in the respective file. If
    the template has no format args, all ESDs will go into one py file. Use - to output to stdout.
-writebnd DIR
    Given Python inputs (with -i), and also ESD inputs (with -esddir or -i), write copies of those
    ESD/bnd files to the given directory if they have compiled ESDs. If the given directory is a
    relative path and gamedir is also provided, it will be relative to the game directory. Can be
    used to write out final files for a mod. This does not create backups. Does not yet handle
    chresdbnds in DS1 chr.
-writeloose TEMPLATE
    Writes out individual .esd files. If there are Python inputs (with -i), there also must be
    ESD inputs (with -esddir or -i) to use as a template; then writes out individual .esd files
    contained in those Python files. If there is more than one .esd, the template must include
    %e, which is the ESD id. If not given any Python files, just writes out the given ESD
    bnds/dcxs as individual .esd files.
-info
    Print basic info on the given input files - some parsing but no compilation/decompilation.
-mapinfo
    For the current game flags, print info about where all ESDs are used. Only supported if -maps
    is supported.

> Compilation options
-[no]cfg
    When enabled (default true), writes state machines as functions with nesting and loops. When
    disabled uses many gotos instead. CFG representation currently excludes unreachable states.
    Until supported, use nocfg to help with cut content recovery.
-[no]stateinfo
    When enabled (default true), writes state ids as docstrings. This is more cluttered but allows
    writing back commands/conditions to the same states.
-[no]newstates
    When enabled (default true), allows creating states with fresh ids, rather than getting all ids
    from docstrings (with -stateinfo).
-[no]talk
    When enabled (default true), use talk ESD commands and functions. Otherwise, uses chr ESD.
    Disable this for ESDs in chr directory in DS1.

> Some examples
Decompile all ESDs for a game to one Python file:
    $ esdtool.exe -ds3 -writepy ds3.py
Decompile all ESDs for a game to different Python files:
    $ esdtool.exe -ds1r -writepy %e.py
Replace game talkesdbnds with the given compiled Python files:
    $ esdtool.exe -sdt -i *.py -writebnd mymod\script\talk
";
        }

        private void ClearFilters()
        {
            Chrs.Clear();
            Maps.Clear();
            Esds.Clear();
        }

        public static ESDOptions Parse(string[] cargs)
        {
            HashSet<char> invalid = new HashSet<char>(Path.GetInvalidPathChars());
            Queue<string> args = new Queue<string>(cargs);
            List<Option> opts = new List<Option>();
            bool isFlag(string arg)
            {
                // - by itself can be a valid arg
                return arg.Length > 1 && arg.StartsWith("-");
            }
            while (args.Count > 0)
            {
                string arg = args.Dequeue();
                if (!isFlag(arg)) throw new Exception($"Expected flag; got argument -{arg}");
                arg = arg.Substring(1);
                string getOnlyArg()
                {
                    if (args.Count == 0 || isFlag(args.Peek())) throw new Exception($"No value provided for flag -{arg}");
                    return args.Dequeue();
                }
                List<string> getMultiArg()
                {
                    List<string> ret = new List<string>();
                    while (args.Count > 0 && !isFlag(args.Peek()))
                    {
                        ret.Add(args.Dequeue());
                    }
                    if (ret.Count == 0) throw new Exception($"No value provided for flag -{arg}");
                    return ret;
                }
                void checkFilename(string path)
                {
                    if (invalid.Overlaps(path)) throw new Exception($"Invalid filename {path}");
                }
                Regex format = new Regex("%.");
                void checkTemplate(string path, string formats)
                {
                    foreach (Match m in format.Matches(path))
                    {
                        char ch = m.Groups[0].Value[1];
                        if (!formats.Contains(ch)) throw new Exception($"Unknown format %{ch} for flag -{arg}");
                    }
                }
                if (games.ContainsKey(arg))
                {
                    opts.Add(new SetGame { Game = games[arg] });
                }
                else if (specFlags.Contains(arg))
                {
                    SetGameOpt opt = new SetGameOpt { Name = arg };
                    string val = getOnlyArg();
                    if (arg == "outdcx")
                    {
                        if (!dcxs.ContainsKey(val.ToLower())) throw new Exception($"Unrecognized {arg} {val} - expected {string.Join(", ", dcxs.Keys)}");
                        opt.Dcx = dcxs[val.ToLower()];
                    }
                    else
                    {
                        opt.Value = val;
                    }
                    opts.Add(opt);
                }
                else if (allFlags.Contains(arg))
                {
                    bool val = true;
                    if (!yesFlags.Contains(arg))
                    {
                        arg = arg.Substring(2);
                        val = false;
                    }
                    opts.Add(new SetFlag { Name = arg, Value = val });
                }
                else if (arg == "f")
                {
                    List<string> vals = getMultiArg();
                    foreach (string val in vals)
                    {
                        // TODO: Add support for enemyCommon and chresdbnds
                        if (!(val.StartsWith("t") || val.StartsWith("c") || val.StartsWith("m") || val.EndsWith("dummy") || val == "enemyCommon")) throw new Exception($"Unrecognized filter value {val}");
                    }
                    opts.Add(new AddFilter { Name = vals });
                }
                else if (arg == "i")
                {
                    List<string> vals = getMultiArg();
                    foreach (string val in vals)
                    {
                        checkFilename(val);
                    }
                    opts.Add(new AddInput { Name = vals });
                }
                else if (arg == "writebnd")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    opts.Add(new WriteBnd { DirName = val });
                }
                else if (arg == "writeloose")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    checkTemplate(val, "e");
                    opts.Add(new WriteLoose { Template = val });
                }
                else if (arg == "writepy")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    checkTemplate(val, "ecm");
                    opts.Add(new WritePy { Template = val });
                }
                else if (arg == "info")
                {
                    opts.Add(new Info());
                }
                else if (arg == "mapinfo")
                {
                    opts.Add(new MapInfo());
                }
                else throw new Exception($"Unknown command line flag -{arg}");
            }
            return new ESDOptions(opts);
        }

        public Option NextAction()
        {
            while (opts.Count > 0)
            {
                Option opt = opts.Dequeue();
                if (opt is SetGame game)
                {
                    Spec = ForGame(game.Game);
                    EsdInputs.Clear();
                    ClearFilters();
                }
                else if (opt is SetGameOpt gameOpt)
                {
                    string val = gameOpt.Value;
                    switch (gameOpt.Name)
                    {
                        case "basedir": Spec.GameDir = val; break;
                        case "esddir":
                            Spec.EsdDir = val;
                            EsdInputs.Clear();
                            ClearFilters();
                            break;
                        case "maps": Spec.MsbDir = val; break;
                        case "names": Spec.NameDir = val; break;
                        case "msgs": Spec.MsgDir = val; break;
                        case "layouts": Spec.LayoutDir = val; break;
                        case "params": Spec.ParamFile = val; break;
                        case "outdcx": Spec.Dcx = gameOpt.Dcx; break;
                        default: break;
                    }
                    if (Spec.GameDir == null) throw new Exception($"Can't set {gameOpt.Name} without setting basedir first");
                }
                else if (opt is SetFlag flag)
                {
                    Flags[flag.Name] = flag.Value;
                }
                else if (opt is AddFilter filter)
                {
                    ClearFilters();
                    foreach (string val in filter.Name)
                    {
                        if (val.StartsWith("m"))
                        {
                            Maps.Add(val);
                        }
                        else if (val.StartsWith("t") || val.EndsWith("dummy") || val == "enemyCommon")
                        {
                            Esds.Add(val);
                        }
                        else if (val.StartsWith("c"))
                        {
                            Chrs.Add(val);
                        }
                        else throw new Exception($"Internal error: unknown filter {val}");
                    }
                }
                else if (opt is AddInput input)
                {
                    if (input.Name.Any(n => n.EndsWith(".py")))
                    {
                        if (!input.Name.All(n => n.EndsWith(".py"))) throw new Exception($"Some but not all input files ended in .py");
                        PyInputs.Clear();
                        PyInputs.AddRange(input.Name);
                    }
                    else
                    {
                        foreach (string val in input.Name)
                        {
                            if (!(val.EndsWith(".esd") || val.EndsWith("esdbnd.dcx") || val.EndsWith(".esd.dcx")))
                            {
                                throw new Exception($"ESD input files must end in .esd, .esdbnd.dcx, or .esd.dcx");
                            }
                        }
                        EsdInputs.Clear();
                        EsdInputs.AddRange(input.Name);
                    }
                }
                else
                {
                    // All others are actions
                    LastAction = opt;
                    return LastAction;
                }
            }
            if (LastAction == null)
            {
                LastAction = new Info();
                return LastAction;
            }
            return null;
        }

        public abstract class Option { }
        public class SetGame : Option
        {
            public FromGame Game { get; set; }
        }
        public class SetGameOpt : Option
        {
            public string Name { get; set; }
            public string Value { get; set; }
            public DCX.Type Dcx { get; set; }
        }
        public class SetFlag : Option
        {
            public string Name { get; set; }
            public bool Value { get; set; }
        }
        public class AddFilter : Option
        {
            public List<string> Name { get; set; }
        }
        public class AddInput : Option
        {
            public List<string> Name { get; set; }
        }
        public class WriteBnd : Option
        {
            public string DirName { get; set; }
        }
        public class WriteLoose : Option
        {
            public string Template { get; set; }
        }
        public class WritePy : Option
        {
            public string Template { get; set; }
        }
        public class Info : Option { }
        public class MapInfo : Option { }
    }
}
