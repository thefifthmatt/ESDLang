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
using static ESDLang.Script.Util;

namespace ESDLang.Script
{
    public class ESDOptions
    {
        // Options to process
        public Queue<Option> opts = new Queue<Option>();
        // State
        public Dictionary<string, bool> Flags = new Dictionary<string, bool>(defaultFlags);
        public bool Flag(string name) => Flags[name];
        public List<string> ChrFilters = new List<string>();
        public List<string> MapFilters = new List<string>();
        public List<string> EsdFilters = new List<string>();
        public List<string> PyInputs = new List<string>();
        public List<string> EsdInputs = new List<string>();
        public Dictionary<string, string> ExtraEsds = new Dictionary<string, string>();
        public string EddDir = null;
        public CmdType Type = CmdType.Unknown;
        public EDDText.EDDFormat EddFormat = EDDText.EDDFormat.Flat;
        public GameSpec Spec = new GameSpec();
        public Option LastAction = null;

        public static readonly EnumOption<FromGame> Games = EnumOption<FromGame>.Create();

        // TODO: Change default... also in accessor function
        private static readonly Dictionary<string, bool> defaultFlags = new Dictionary<string, bool> {
            { "cfg", true },
            { "stateinfo", true },
            { "deadstates", true },
            { "newstates", true },
            { "regsubstitute", true },
            { "cmdedd", false },
            { "copysame", false },
            { "backup", false },
        };
        private static readonly HashSet<string> allFlags = new HashSet<string>(defaultFlags.Keys.Concat(defaultFlags.Keys.Select(f => $"no{f}")));
        private static readonly EnumOption<DCX.Type> dcxs = EnumOption<DCX.Type>.Create();
        private static readonly EnumOption<CmdType> cmdTypes = EnumOption<CmdType>.Create();
        private static readonly EnumOption<EDDText.EDDFormat> eddFormats = EnumOption<EDDText.EDDFormat>.Create();
        private static readonly HashSet<string> specFlags = new HashSet<string> { "basedir", "esddir", "maps", "msgs", "names", "layouts", "defs", "params", "outdcx" };

        public class EnumOption<T>
        {
            public List<T> List { get; set; }
            public Dictionary<string, T> Names { get; set; }
            public static EnumOption<T> Create()
            {
                List<T> list = ((T[])Enum.GetValues(typeof(T))).Where(d => d.ToString().ToLower() != "unknown").ToList();
                return new EnumOption<T>
                {
                    List = list,
                    Names = list.ToDictionary(f => f.ToString().ToLower(), f => f)
                };
            }
            public T this[string val]
            {
                get
                {
                    if (!Names.TryGetValue(val.ToLower(), out T type)) throw new Exception($"Unrecognized {typeof(T).ToString().ToLower()} {val} - expected {string.Join(", ", List)}");
                    return type;
                }
            }
        }

        private ESDOptions(List<Option> opts)
        {
            this.opts = new Queue<Option>(opts);
        }

        public static string GetShortUsage()
        {
            return $@"Usage: esdtool.exe [-h] [{string.Join(" | ", Games.List.Select(g => $"-{g}".ToLower()))}]
                   [-basedir DIR] [-esddir DIR] [-maps DIR] [-msgs DIR] [-params FILE] [-names DIR]
                   [-layouts DIR] [-outdcx DCXTYPE] [-i FILE1 FILE2 etc] [-f ESD MAP CHR etc] [-extra ESD=BND etc]
                   [-[no]cfg] [-[no]stateinfo] [-[no]deadstates] [-[no]newstates] [-[no]regsubstitute]
                   [-[no]cmdedd] [-[no]copysame] [-[no]backup] [-cmdtype TYPE] [-edddir DIR]
                   [-writepy TEMPLATE] [-writebndfile FILE] [-writebndfile DIR] [-writeloose TEMPLATE]
                   [-writeedd DIR] [-info]
";
        }

        public static string GetUsage()
        {
            return $@"Usage: esdtool.exe <args>

esdtool decompiles ESDs to a high-level Python representation, which can be compiled back to ESD.
Similar to ffmpeg or ImageMagick, the order of command line arguments determines the order of
operations. For instance, -ds1 -esddir chr will default everything to DS1, but then change
the subdirectory used for ESD inputs. The other way around will not work.

> Game flag
{string.Join(", ", Games.List.Select(g => $"-{g}".ToLower()))}
    Sets all game data flags to default known values for Steam installations of the given game, or
    clears them if unknown. This overrides all values which were there before. These default values
    are kept in SoulsIds in GameSpec.cs

> Game data flags
(not necessary to set if set by the game flag)
-basedir DIR
    Sets the base directory for esddir, maps, msgs, and params. UXM or similar tool must be used.
-esddir DIR
    Sets the relative dir for all ESDs, meaning all .esd, .esd.dcx, and esdbnd.dcx files in
    that directory. Overrides -i for a list of ESDs and clears -f.
-maps DIR
    Sets the relative dir for all MSB files. Used to look up chr info on ESDs, currently for
    DS1, DS1R, DS3, and Sekiro.
-msgs DIR
    Sets the relative dir where FMG bnds can be found. Used to annotate ESDs with game info.
-params FILE
    Sets the relative file with game params. Used to annotate ESDs with game info.
    Requires -layouts or -defs.
-names DIR
    A directory with names for game ids. Currently ModelName.txt is used alongside chr info.
-layouts DIR
    A directory with layout xml files, required to use -params in most games.
-defs DIR
    A directory with paramdef xml files, required to use -params in Elden Ring.
-outdcx [{string.Join(" | ", dcxs.List)}]
    Sets the DCX type to use when writing ESDs (writebnd/writeloose).

> Input/output flags
-i FILE1 FILE2 etc
    Can be used in two ways, for a list of one or more files. If all files end in .py, sets
    the list of Python files to compile. If all files end in .esd, .esd.dcx, and esdbnd.dcx,
    sets the list of ESD files to decompile; also overrides -esddir and clears -f. These are
    relative to the current directory if relative paths.
-f ESD MAP CHR etc
    A list of one or more filters for -esddir or -i inputs, replacing previous list of filters
    (if any). ESD is an ESD name or prefix (like t300330 or event), MAP is a prefix for a BND
    name (like m40_00), and CHR is a character model with an ESD (like c1400, if -maps is
    supported). The ESDs output/replaced are a union of all filters. Filters do nothing if no
    input ESD matches them.
-edddir DIR
    The directory to use to find .edd or .edd.txt files, default dist\<game>\edd when it exists
    for English translations. This can be set to the same as -esddir to use the original EDD files.
-[no]backup
    When enabled (default false), backs up files with a .bak suffix before writing them. If the
    .bak file already exists, this does nothing. This is usually not needed if you're using a
    separate mod directory.
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
    used to write out final files for a mod.
-writebndfile FILE
    Same as -writebnd, but it will only write to the given BND file. It will still compile all
    inputs. If the given directory is a relative path and gamedir is also provided, it will be
    relative to the game directory.
-extra ESD1=BND2 ESD2=BND2 etc
    Used with -writebnd to add extra ESD files not present in the original game ESDs. For example,
    if the -writebnd directory contains m10_00_00_00.talkesdbnd.dcx, you can add a new ESD t100630
    to it by specifying t100630=m10_00_00_00
-[no]copysame
    When enabled (default false), writebnd not only writes copied of the compiled ESDs, but also
    copies of all ESDs which are identical to it. This can be used to decompile only one bonfire
    and change all other bonfires at once. Equivalence is determined an ESD's hash, which is shown
    by -info.
-writeloose TEMPLATE
    Writes out individual .esd files. If there are Python inputs (with -i), there also must be
    ESD inputs (with -esddir or -i) to use as a template; then writes out individual .esd files
    contained in those Python files. If there is more than one .esd, the template must include
    %e, which is the ESD id. If not given any Python files, just writes out the given ESD
    bnds/dcxs as individual .esd files.
-writeedd TEMPLATE
    Writes out .edd.txt files for EDD files alongside input ESD files, which can be used to
    annotate Python files with developer documentation. %e is the ESD id. Translated EDD dumps are
    already included with esdtool so this is not usually necessary.
-info
    Print basic info on the given input files - some parsing but no compilation/decompilation.
    If -maps is supported, also prints where the ESDs are used.

> EDD writing options
-eddformat {string.Join(" | ", eddFormats.List)}
    How to write .edd.txt files. This can be done flat (basically a direct dump), chunked with
    all strings in shared files at most 500 lines long, or joining chunked inputs from -edddir.

> Compilation options
-[no]cfg
    When enabled (default true), writes state machines as functions with nesting and loops. When
    disabled uses many gotos instead. CFG representation currently excludes unreachable states.
    Until supported, use nocfg to help with cut content recovery.
-[no]stateinfo
    When enabled (default true), writes state ids as docstrings. This is more cluttered but allows
    writing back commands/conditions to the same states.
-[no]deadstates
    When enabled (default true), adds unreachable states at the end of machines. This has no effect
    on execution, and it can be noisy, but it can also be helpful for restoring cut content.
-[no]newstates
    When enabled (default true), allows creating states with fresh ids, rather than requiring tha
    all all ids are specified in docstrings (with -stateinfo).
-[no]regsubstitute
    When enabled (default true), decompilation substitutes GetREG expressions with the contents of
    equivalent SetREG expressions from within the same state. The reverse optimization is not
    currently done during compilation.
-[no]cmdedd
    When enabled (default false) and EDD is available, output text for each individual command
    where given a description. This appears to be automatically inserted based on the command id,
    rather than custom text like state or machine descriptions.
-cmdtype [{string.Join(" | ", cmdTypes.List)}]
    The source to use for command and function names, for both reading and writing. If not
    provided, this is inferred from .esd/.py name and provided game where possible. Otherwise, None
    is used.

> Some examples
Show all known ESDs for a game:
    $ esdtool.exe -ds2s
Decompile all ESDs for a game to one Python file:
    $ esdtool.exe -ds3 -writepy ds3.py
Decompile all ESDs for a game to different Python files:
    $ esdtool.exe -ds1r -writepy %e.py
Decompile a specific ESD from a game by name:
    $ esdtool.exe -sdt -f t000001 -writepy %e.py
Decompile and recompile a lone ESD file (cmd type inferred from name):
    $ esdtool.exe -ds2s -i work\event_m10_04_00_00.esd -writepy work\%e.py
    $ esdtool.exe -ds2s -i work\event_m10_04_00_00.py -writeloose work\%e_recompiled.esd
Recompile the given Python files into a subdirectory of the game, copying relevant bnds:
    $ esdtool.exe -sdt -i *.py -writebnd mymod\script\talk
    $ esdtool.exe -ds2s -i mymod\event_m10_04_00_00.py -writebnd mymod\ezstate
";
        }

        private void ClearFilters()
        {
            ChrFilters.Clear();
            MapFilters.Clear();
            EsdFilters.Clear();
        }

        public static ESDOptions Parse(IList<string> cargs)
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
                if (Games.Names.ContainsKey(arg))
                {
                    opts.Add(new SetGame { Game = Games.Names[arg] });
                }
                else if (specFlags.Contains(arg))
                {
                    SetGameOpt opt = new SetGameOpt { Name = arg };
                    string val = getOnlyArg();
                    if (arg == "outdcx")
                    {
                        opt.Dcx = dcxs[val.ToLower()];
                    }
                    else
                    {
                        opt.Value = val;
                    }
                    opts.Add(opt);
                }
                else if (arg == "cmdtype")
                {
                    string val = getOnlyArg();
                    opts.Add(new SetCmdType { Type = cmdTypes[val] });
                }
                else if (arg == "eddformat")
                {
                    string val = getOnlyArg();
                    opts.Add(new SetEddFormat { Type = eddFormats[val] });
                }
                else if (arg == "edddir")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    opts.Add(new SetEddDir { DirName = val });
                }
                else if (allFlags.Contains(arg))
                {
                    bool val = true;
                    if (!defaultFlags.ContainsKey(arg))
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
                        if (!(val.StartsWith("c") || val.StartsWith("h") || val.StartsWith("m") || ESDName.IsKnownPrefix(val))) throw new Exception($"Unrecognized filter value {val}");
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
                else if (arg == "extra")
                {
                    List<string> vals = getMultiArg();
                    Dictionary<string, string> extra = new Dictionary<string, string>();
                    foreach (string val in vals)
                    {
                        string[] parts = val.Split('=');
                        if (parts.Length != 2) throw new Exception($"Arg {val} for -extra requires format ESD=BND");
                        extra[parts[0]] = parts[1];
                    }
                    opts.Add(new AddExtraEsds { Names = extra });
                }
                else if (arg == "writebndfile")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    opts.Add(new WriteBnd { FileName = val });
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
                else if (arg == "writeedd")
                {
                    string val = getOnlyArg();
                    checkFilename(val);
                    checkTemplate(val, "e");
                    if (!val.EndsWith(".edd.txt")) throw new Exception("writeedd argument does not end with .edd.txt");
                    opts.Add(new WriteEdd { Template = val });
                }
                else if (arg == "info")
                {
                    opts.Add(new Info());
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
                    ExtraEsds.Clear();
                    ClearFilters();
                }
                else if (opt is SetGameOpt gameOpt)
                {
                    string val = gameOpt.Value;
                    switch (gameOpt.Name)
                    {
                        case "basedir": Spec.GameDir = WindowsifyPath(val); break;
                        case "esddir":
                            Spec.EsdDir = WindowsifyPath(val);
                            EsdInputs.Clear();
                            ClearFilters();
                            break;
                        case "maps": Spec.MsbDir = val; break;
                        case "names": Spec.NameDir = val; break;
                        case "msgs": Spec.MsgDir = val; break;
                        case "layouts": Spec.LayoutDir = WindowsifyPath(val); break;
                        case "defs": Spec.DefDir = WindowsifyPath(val); break;
                        case "params": Spec.ParamFile = WindowsifyPath(val); break;
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
                        if (ESDName.IsKnownPrefix(val))
                        {
                            EsdFilters.Add(val);
                        }
                        else if (val.StartsWith("m"))
                        {
                            MapFilters.Add(val);
                        }
                        else if (val.StartsWith("c") || val.StartsWith("h"))
                        {
                            ChrFilters.Add(val);
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
                else if (opt is AddExtraEsds extra)
                {
                    foreach (KeyValuePair<string, string> entry in extra.Names)
                    {
                        ExtraEsds[entry.Key] = entry.Value;
                    }
                }
                else if (opt is SetCmdType cmd)
                {
                    Type = cmd.Type;
                }
                else if (opt is SetEddFormat eddFormat)
                {
                    EddFormat = eddFormat.Type;
                }
                else if (opt is SetEddDir eddDir)
                {
                    EddDir = eddDir.DirName;
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
        public class SetCmdType : Option
        {
            public CmdType Type { get; set; }
        }
        public class SetEddFormat : Option
        {
            public EDDText.EDDFormat Type { get; set; }
        }
        public class SetEddDir : Option
        {
            public string DirName { get; set; }
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
        public class AddExtraEsds : Option
        {
            public Dictionary<string, string> Names { get; set; }
        }
        public class WriteBnd : Option
        {
            public string DirName { get; set; }
            public string FileName { get; set; }
        }
        public class WriteLoose : Option
        {
            public string Template { get; set; }
        }
        public class WritePy : Option
        {
            public string Template { get; set; }
        }
        public class WriteEdd : Option
        {
            public string Template { get; set; }
        }
        public class Info : Option { }

        public enum CmdType { Unknown, None, Talk, TalkER, Chr, Event, AI }
    }
}
