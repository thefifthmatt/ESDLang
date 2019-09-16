using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static SoulsIds.GameSpec;
using static ESDLang.Script.ESDOptions;

namespace ESDLang.Script
{
    public class ESDName
    {
        // For now, just a bunch of static methods. Could this make sense as an instantiable object?
        private static HashSet<string> exactChr = new HashSet<string> { "c0000", "enemyCommon" };
        private static List<Regex> prefixes = new[] { @"t(\d{6})?", @"event(_m\d\d(_\d\d(_00_00)?)?)?", @"talk(_m\d\d(_\d\d(_00_00)?)?)?", @"ai(\d{6})?", @"dummy(_m\d\d)?" }.Select(s => new Regex($"^{s}$")).ToList();
        public static bool IsKnownPrefix(string name)
        {
            if (exactChr.Contains(name)) return true;
            return prefixes.Any(p => p.IsMatch(name));
        }
        private static Dictionary<FromGame, CmdType> defaultCmds = new Dictionary<FromGame, CmdType>
        {
            [FromGame.DS1] = CmdType.Talk,
            [FromGame.DS1R] = CmdType.Talk,
            [FromGame.BB] = CmdType.Talk,
            [FromGame.DS3] = CmdType.Talk,
            [FromGame.SDT] = CmdType.Talk,
            [FromGame.DS2] = CmdType.Event,
            [FromGame.DS2S] = CmdType.Event,
        };
        public static CmdType GetCmdType(string esd, FromGame game = FromGame.UNKNOWN)
        {
            if (esd.StartsWith("talk") || esd.StartsWith("event")) return CmdType.Event;
            if (esd.StartsWith("ai")) return CmdType.AI;
            if (esd.StartsWith("t")) return CmdType.Talk;
            if (esd.StartsWith("dummy") || exactChr.Contains(esd)) return CmdType.Chr;
            if (defaultCmds.TryGetValue(game, out CmdType type)) return type;
            return CmdType.None;
        }
        public static string ToFunctionPrefix(string esd)
        {
            if (Regex.IsMatch(esd, @"(event|talk)_m\d\d_\d\d_00_00"))
            {
                return esd.Replace("_00_00", "");
            }
            return esd;
        }
        public static string FromFunctionPrefix(string esd)
        {
            if (Regex.IsMatch(esd, @"(event|talk)_m\d\d_\d\d"))
            {
                return esd + "_00_00";
            }
            return esd;
        }
        // Function is up to 3 parts: ESD name, comment (if ESD name is recognized), and machine name.
        private static List<Regex> esdNames = new[] { @"t\d{6}", @"event_m\d\d_\d\d(_00_00)?", @"talk_m\d\d_\d\d(_00_00)?", @"ai\d{6}", @"dummy_m\d\d" }.Concat(exactChr).Select(s => new Regex($"^{s}_")).ToList();
        public static (string, string) ParseFunction(string func)
        {
            foreach (Regex esdName in esdNames)
            {
                Match match = esdName.Match(func);
                if (match.Success)
                {
                    return (func.Substring(0, match.Length - 1), func.Split('_').Last());
                }
            }
            int index = func.LastIndexOf('_');
            if (index == -1) return (func, "");
            return (func.Substring(0, index), func.Substring(index + 1));
        }
    }
}
