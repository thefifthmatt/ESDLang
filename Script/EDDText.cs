﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using SoulsFormats;
using static SoulsFormats.EDD;

namespace ESDLang.Script
{
    public class EDDText
    {
        public enum EDDFormat
        {
            Flat,
            Chunk,
            Join,
        }

        // The EDD itself
        public EDD edd { get; set; }
        // Map from to machine/state id to unique string index
        private Dictionary<string, int> locs = new Dictionary<string, int>();
        // All unique strings. These may be shared across multiple instances of EDDText
        private List<string> order;

        public EDDText() { }

        private string OptString(string id) => locs.TryGetValue(id, out int loc) ? order[loc] : null;
        public string MachineName(string id) => OptString(id);
        public string MachineParam(string id, int i) => OptString($"{id}_p{i}");
        public string State(string id, int state) => OptString($"{id}_s{state}");
        public string Command(string id, int state, string type, int i) => OptString($"{id}_s{state}_{type}{i}");

        public static void ReadEddStrs(string dir, List<string> order)
        {
            int i = 0;
            order.Clear();
            while (true)
            {
                string path = $@"{dir}\s{i:d3}.txt";
                if (!File.Exists(path)) return;
                order.AddRange(File.ReadLines(path));
                i++;
            }
        }

        public static void WriteEddStrs(string dir, List<string> order, int chunkSize)
        {
            foreach (string path in Directory.EnumerateFiles(dir, "s*.txt").ToList())
            {
                File.Delete(path);
            }
            for (int start = 0; start < order.Count; start += chunkSize)
            {
                using (TextWriter writer = File.CreateText($@"{dir}\s{start / chunkSize:d3}.txt"))
                {
                    int limit = Math.Min(start + chunkSize, order.Count);
                    for (int i = start; i < limit; i++)
                    {
                        writer.WriteLine(order[i]);
                    }
                }
            }
        }

        private static (int, string) DumpXml(bool command, int id, string name)
        {
            return (id + (command ? 100000 : 0), $"        <{(command ? "Command" : "Function")} {(command ? "Bank=\"1\" " : "")}ID=\"{id}\" Name=\"{name}\" Description=\"\"/>");
        }

        // Writes to the given path, or if chunks are involved, selects multiple paths. Does not write strings in chunks.
        public void Write(string path, EDDFormat format)
        {
            if (format == EDDFormat.Chunk)
            {
                string part = path.Replace(".edd.txt", "");
                using (TextWriter writer = File.CreateText(part + "_part.edd.txt"))
                {
                    // Also call WriteEddStrs alongside this
                    foreach (KeyValuePair<string, int> entry in locs)
                    {
                        writer.WriteLine($"{entry.Key}: #{entry.Value}");
                    }
                }
            }
            else
            {
                using (TextWriter writer = File.CreateText(path))
                {
                    if (edd != null)
                    {
                        List<(int, string)> xmls = new List<(int, string)>();
                        foreach (FunctionSpec f in edd.FunctionSpecs)
                        {
                            writer.WriteLine($"f{f.ID:d3}: {f.Name}");
                            xmls.Add(DumpXml(false, f.ID, f.Name));
                        }
                        foreach (CommandSpec f in edd.CommandSpecs)
                        {
                            writer.WriteLine($"c{f.ID:d3}: {f.Name}");
                            xmls.Add(DumpXml(true, (int)f.ID, f.Name));
                        }
                        // Informal utility to generate XML
                        // writer.WriteLine(string.Join("\r\n", xmls.OrderBy(s => s).Select(s => s.Item2)));
                    }
                    foreach (KeyValuePair<string, int> entry in locs)
                    {
                        writer.WriteLine($"{entry.Key}: {order[entry.Value]}");
                    }
                }
            }
        }

        public void ReadTxt(string path, List<string> sharedStrings = null)
        {
            // Two cases: either a single .edd.txt file, or chunks to join together and rely on shared strings.
            bool strRef = sharedStrings != null;
            order = sharedStrings ?? new List<string>();
            if (strRef) path = path.Replace(".edd.txt", "_part.edd.txt");
            Dictionary<int, MachineDesc> machines = new Dictionary<int, MachineDesc>();
            foreach (string line in File.ReadLines(path))
            {
                if (line.Length == 0) continue;
                string[] parts = line.Split(new[] { ' ' }, 2);
                if (parts.Length != 2 || !parts[0].EndsWith(":") || parts[1].StartsWith("#") != strRef) throw new Exception($"{path}: bad line: {line}");
                string desc = parts[0].Substring(0, parts[0].Length - 1);
                if (strRef)
                {
                    locs[desc] = int.Parse(parts[1].Substring(1));
                }
                else
                {
                    addStr(desc, parts[1]);
                }
                string name = order[locs[desc]];
                parts = desc.Split('_');
                // These should just be command names
                if (desc.StartsWith('c') || desc.StartsWith('f')) continue;
                if (!Common.ParseMachine(parts[0], out int machineId)) throw new Exception($"Bad machine id in {desc}");
                if (!machines.TryGetValue(machineId, out MachineDesc machine))
                {
                    machine = machines[machineId] = new MachineDesc(machineId);
                }
                if (parts.Length == 1)
                {
                    machine.Name = name;
                }
                else
                {
                    int i = int.Parse(parts[1].Substring(1));
                    if (parts[1].StartsWith("p"))
                    {
                        machine.ParamNames[i] = name;
                    }
                    else if (parts[1].StartsWith("s"))
                    {
                        StateDesc state = machine.States.Find(s => s.ID == i);
                        if (state == null)
                        {
                            state = new StateDesc(i);
                            machine.States.Add(state);
                        }
                        if (parts.Length == 2)
                        {
                            state.Name = name;
                        }
                        else
                        {
                            // Ignore indices, add in order
                            if (parts[2].StartsWith("e")) state.EntryCommands.Add(new CommandDesc(name));
                            else if (parts[2].StartsWith("x")) state.ExitCommands.Add(new CommandDesc(name));
                            else if (parts[2].StartsWith("w")) state.WhileCommands.Add(new CommandDesc(name));
                        }
                    }
                    else throw new Exception(desc);
                }
            }
            edd = new EDD();
            edd.Machines = machines.Values.ToList();
        }

        private void addStr(string desc, string text)
        {
            int index = order.IndexOf(text);
            if (index == -1)
            {
                order.Add(text);
                index = order.Count - 1;
            }
            locs[desc] = index;
        }

        public void ReadEDD(string path, List<string> sharedStrings = null)
        {
            // Read the given EDD. If shared strings is provided, we should dump our strings into it.
            try
            {
                edd = EDD.Read(path);
            }
            catch (Exception e)
            {
                // Some format errors, not everything is known yet
                Console.WriteLine($"Error reading {path}: {e}");
                return;
            }
            order = sharedStrings ?? new List<string>();
            // 1179 at the start. 1101 with builtin dedupe
            // return;
            List<string> s = new List<string>();
            foreach (MachineDesc machine in edd.Machines)
            {
                string m = Common.FormatMachine(machine.ID);
                addStr(m, machine.Name);
                for (int i = 0; i < machine.ParamNames.Length; i++)
                {
                    string text = machine.ParamNames[i];
                    if (text == null) continue;
                    addStr($"{m}_p{i}", text);
                }
                foreach (StateDesc state in machine.States)
                {
                    addStr($"{m}_s{state.ID}", state.Name);
                    void WriteCommands(List<CommandDesc> cmds, string prefix)
                    {
                        for (int i = 0; i < cmds.Count; i++)
                        {
                            addStr($"{m}_s{state.ID}_{prefix}{i}", cmds[i].Name);
                        }
                    }
                    WriteCommands(state.EntryCommands, "e");
                    WriteCommands(state.ExitCommands, "x");
                    WriteCommands(state.WhileCommands, "w");
                    for (int i = 0; i < state.PassCommands.Count; i++)
                    {
                        WriteCommands(state.PassCommands[i].PassCommands, $"p{i}_");
                    }
                }
            }
        }
    }
}
