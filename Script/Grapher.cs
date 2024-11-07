#if !X
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using static ESDLang.EzSemble.AST;
using static ESDLang.Script.Util;
using static ESDLang.Script.Common;
using static ESDLang.Script.ESDOptions;
using System.IO;
using Microsoft.Scripting.ComInterop;
using SoulsIds;

namespace ESDLang.Script
{
    public class Grapher
    {
        private readonly Universe u;
        private readonly Decompiler decompiler;

        public Grapher(Universe u, Decompiler decompiler)
        {
            this.u = u;
            this.decompiler = decompiler;
        }

        public void Graph(object esd, string machineId)
        {
            ESDStructure structure = decompiler.ProcessESD(esd, shortCall: true);

            // Perform decompilation per machine
            foreach (KeyValuePair<int, SortedDictionary<int, State>> machineEntry in structure.Machines.OrderBy(e => MachineSort(e.Key)))
            {
                int machine = machineEntry.Key;
                SortedDictionary<int, State> states = machineEntry.Value;

                if (FormatMachine(machine) != machineId) continue;

                // TODO: Use PrintProgram state in ToString stuff
                // PrintProgram(esdId, m, structure.MachineArgs[machine], structure.GlobalReplace);
                WriteGraph(structure, states);
            }
        }

        private void WriteGraph(ESDStructure structure, SortedDictionary<int, State> states)
        {
            // Use CFG only for this order.
            // Earlier entries should be always higher up than later ones
            // TODO maybe even do this in structure order?
            Decompiler.CFG stateCfg = Decompiler.CFG.FromStates(states);
            // This should also ignore unreachable states
            List<int> order = stateCfg.GetPreorder();
            Dictionary<string, int> orderDict = order.Select((n, i) => (n, i)).ToDictionary(e => $"s{e.Item1}", e => e.Item2);

            // bool bi = true;
            TextWriter dot = File.CreateText(@"graph.dot");
            dot.WriteLine($"digraph {{");
            dot.WriteLine("  nodesep=0.2;"); // 0.25
            dot.WriteLine("  ranksep=0.5;"); // 0.5 or 0.7
            string fontsize = "";
            // fontsize = ",fontsize=\"20pt\"";
            dot.WriteLine("  node [ fontsize=16,width=0.1,height=0.1 ];");
            // dot.WriteLine("  rankdir=\"LR\";");
            // dot.WriteLine("  ratio=1; ");
            string escape(object o)
            {
                if (o == null) return "";
                return o.ToString().Replace("\n", "\\l").Replace("\"", "\\\"") + "\\l";
            }
            // Make shared nontrivial conditions their own nodes. For now, only top-level ones
            HashSet<int> sharedConds = new();
            foreach (int stateId in order)
            {
                State state = states[stateId];
                foreach (Condition cond in state.Conditions)
                {
                    // TODO deal with cond.Pass, but this is limited mainly to debug statements
                    if (cond.DupeID is int dupeId && dupeId >= 0 && cond.Expr != null)
                    {
                        sharedConds.Add(dupeId);
                        int leastState = cond.Flatten()
                            .Select(alt => alt.Last().TargetState ?? -1)
                            .Where(s => s >= 0)
                            .OrderBy(s => orderDict[$"s{s}"])
                            .FirstOrDefault(state.ID);
                        orderDict[$"d{dupeId}"] = orderDict[$"s{leastState}"];
                    }
                }
            }

            bool isReturn(State state, out int val)
            {
                val = -1;
                if (state.Conditions.Count == 1 && state.Conditions[0].Pass is Block pb
                    && pb.Cmds.Count == 1 && pb.Cmds[0].Name == "7:-1")
                {
                    val = pb.Cmds[0].Args[0].AsInt();
                    return true;
                }
                return false;
            }
            // bool onlyCore = false;
            foreach (int stateId in order)
            {
                State state = states[stateId];
                string shape = stateId == 0 ? "box3d" : "box";
                string color = null;
                // Other colors: lightblue pink lightgray
                string fill = "";
                if (color != null) fill = $",style=filled,fillcolor={color}";
                List<string> lines = new List<string>();
                if (state.Entry != null)
                {
                    foreach (Statement st in state.Entry.Cmds)
                    {
                        lines.AddRange(WriteSourceInfo(new PrintData(u, null), statement: st).Select(comment));
                        lines.Add(WriteStatement("", st, structure.GlobalReplace));
                    }
                }
                if (isReturn(state, out int val))
                {
                    lines.Add($"return {val}");
                }
                string label = string.Join("\n", lines);
                dot.WriteLine($"    \"s{stateId}\" [ shape={shape},label=\"{escape(label)}\"{fill} ];");
            }
            foreach (int dupeId in sharedConds)
            {
                dot.WriteLine($"    \"d{dupeId}\" [ shape=diamond,label=\"\" ];");
            }
            HashSet<int> addedConds = new();
            // Improvements:
            // DONE (as hover): State ids
            // DONE (pyprint): Remove AbortIfFalse
            // Add annotations
            // Add enums to conditions
            // Fix machine calls
            // Add returns
            // Collapse useless nodes
            string comment(string s) => "# " + (s.Replace("\n", " ").Split(" - ")[0]);
            foreach (int stateId in order)
            {
                State state = states[stateId];
                if (isReturn(state, out _)) continue;
                int prevConds = 0;
                foreach (Condition cond in state.Conditions)
                {
                    // In x9
                    // Condition(TargetState=, Expr=#B9 != #BA, Sub=[Condition(TargetState=36, Expr=GetMissionState(2250, 1) == 1, Sub=[], Pass=[])], Pass=[])
                    // Condition(TargetState=, Expr=#B9 != #BA, Sub=[Condition(TargetState=36, Expr=GetEventFlag(8101) == 1, Sub=[], Pass=[])], Pass=[])
                    // Condition(TargetState=, Expr=#B9 != #BA, Sub=[Condition(TargetState=30, Expr=, Sub=[], Pass=[])], Pass=[]))
                    string startNode = $"s{stateId}";
                    string from, to;
                    if (cond.DupeID is int dupeId && sharedConds.Contains(dupeId))
                    {
                        string dupeNode = $"d{dupeId}";
                        from = startNode;
                        to = dupeNode;
                        // Boilerplate
                        string color = "";
                        string dir = "";
                        if (orderDict[to] < orderDict[from])
                        {
                            (to, from) = (from, to);
                            dir = ",dir=back";
                        }
                        string label = "";
                        string style = "dashed"; // dashed, dotted
                        // color = "color=red"; bold = ",penwidth=3";
                        dot.WriteLine($"  \"{from}\" -> \"{to}\" [ style={style},labelloc=t,label=\"{escape(label)}\"{dir}{fontsize}{color} ];");
                        if (!addedConds.Add(dupeId)) continue;
                        startNode = dupeNode;
                    }
                    foreach (List<Condition> conds in cond.Flatten())
                    {
                        Condition combined = Condition.Combine(conds, true);
                        if (combined.TargetState is null)
                        {
                            // TODO: Return statements
                            // if (combined.Pass != null && combined.Pass.Cmds.Count == 1 && combined.Pass.Cmds[0].Name == "7:-1") continue;
                            throw new Exception($"No target in {combined}");
                        }
                        string targetNode = $"s{combined.TargetState}";
                        from = startNode;
                        to = targetNode;
                        // Boilerplate
                        string color = "";
                        string dir = "";
                        if (orderDict[to] < orderDict[from])
                        {
                            (to, from) = (from, to);
                            dir = ",dir=back";
                        }
                        // if (conds.Count(c => c.Expr != null) > 1) color = ",color=red";
                        List<string> lines = new List<string>();
                        if (combined.Expr is not null)
                        {
                            lines.AddRange(WriteSourceInfo(new PrintData(u, null), expr: combined.Expr).Select(comment));
                            lines.Add(WriteExpr(combined.Expr, structure.GlobalReplace));
                            if (prevConds >= 0) prevConds++;
                        }
                        else if (prevConds > 0)
                        {
                            lines.Add("else");
                            prevConds = -1;
                        }
                        string label = string.Join("\n", lines);
                        string style = "solid"; // dashed, dotted
                        // color = "color=red"; bold = ",penwidth=3";
                        dot.WriteLine($"  \"{from}\" -> \"{to}\" [ style={style},labelloc=t,label=\"{escape(label)}\"{dir}{fontsize}{color} ];");
                    }
                }
            }
            dot.WriteLine("}");
            dot.Close();

        }
    }
}
#endif