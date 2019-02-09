using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace SoulsFormats.ESD.EzSemble
{
    public class EzSembleContext
    {
        public Dictionary<(int Bank, int ID), string> CommandNamesByID;
        public Dictionary<string, (int Bank, int ID)> CommandIDsByName 
            => CommandNamesByID.ToDictionary(kvp => kvp.Value, kvp => kvp.Key);
        public Dictionary<int, string> FunctionNamesByID;
        public Dictionary<string, int> FunctionIDsByName
            => FunctionNamesByID.ToDictionary(kvp => kvp.Value, kvp => kvp.Key);

        public EzSembleContext()
        {
            CommandNamesByID = new Dictionary<(int Bank, int ID), string>();
            FunctionNamesByID = new Dictionary<int, string>();
        }

        public string GetCommandName(int bank, int id)
        {
            if (CommandNamesByID.ContainsKey((bank, id)))
            {
                return CommandNamesByID[(bank, id)];
            }
            else
            {
                return $"{bank}:{id}";
            }
        }

        public (int Bank, int ID) GetCommandID(string name)
        {
            if (CommandIDsByName.ContainsKey(name))
            {
                return CommandIDsByName[name];
            }
            else
            {
                var regex = Regex.Match(name, @"(\d+):(\d+)");
                return (int.Parse(regex.Groups[1].Value), int.Parse(regex.Groups[2].Value));
            }
        }

        public string GetFunctionName(int id)
        {
            if (FunctionNamesByID.ContainsKey(id))
                return FunctionNamesByID[id];
            else
                return $"f{id}";
        }

        public int GetFunctionID(string name)
        {
            if (FunctionIDsByName.ContainsKey(name))
                return FunctionIDsByName[name];
            else
                return int.Parse(name.Substring(1));
        }
    }
}
