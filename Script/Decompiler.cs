using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

using ESDLang.EzSemble;
using SoulsFormats;
using SoulsIds;

using static ESDLang.EzSemble.AST;
using static SoulsIds.Universe;
using static SoulsFormats.EDD;
using static ESDLang.Script.Util;
using static ESDLang.Script.Common;

namespace ESDLang.Script
{
    public class Decompiler
    {
        private readonly EzSembleContext ezContext;
        private readonly ESDOptions options;
        private readonly string esdId;
        private readonly Universe u;
        private readonly EDD edd;
        public Decompiler(EzSembleContext ezContext, ESDOptions options, string esdId, Universe u=null, EDD edd=null)
        {
            this.ezContext = ezContext;
            this.options = options;
            this.esdId = esdId;
            this.u = u;
            this.edd = edd ?? new EDD();
        }

        public void Decompile(ESD esd, TextWriter writer)
        {
            SortedDictionary<int, SortedDictionary<int, State>> machines = new SortedDictionary<int, SortedDictionary<int, State>>();
            Condition getCond(State state, ESD.Condition esdCond, bool sub=false)
            {
                Condition cond = new Condition
                {
                    Inner = esdCond,
                    TargetState = (int?)esdCond.TargetState,
                };
                Expr expr = EzSembler.DissembleExpression(ezContext, esdCond.Evaluator);
                if (!(expr is ConstExpr con && con.Value.ToString().Equals("1")))
                {
                    cond.Expr = expr;
                }
                bool hasPass = false;
                if (esdCond.TargetState != null)
                {
                    state.Next.Add((int)cond.TargetState);
                }
                if (esdCond.Subconditions.Count > 0)
                {
                    cond.Sub = esdCond.Subconditions.Select(e => getCond(state, e, true)).ToList();
                }
                if (esdCond.PassCommands.Count > 0)
                {
                    cond.Pass = EzSembler.DissembleCommandScript(ezContext, esdCond.PassCommands);
                    hasPass = cond.Pass.Cmds.Any(c => c.Name != "DebugLogOutput" && c.Name != "DebugEvent");
                    // In bloodborne, this is perfectly fine
                    // if (hasPass && cond.Expr != null) throw new Exception($"Conditional pass block in {state}\n\n{cond}");
                }
                int modes = (cond.TargetState == null ? 0 : 1) + (cond.Sub.Count == 0 ? 0 : 1) + (hasPass ? 1 : 0);
                // In bloodborne, pass blocks and target states can exit together...
                if (modes == 0 || (cond.Sub.Count > 0 && modes > 1))
                {
                    throw new Exception($"Unexpected condition structure in {esdId} {state}\n\nIssue: {cond}");
                }
                return cond;
            }
            // TODO: Add this as header? So we don't have to rely on baseESD hack
            // Console.WriteLine($"# {esd.LongFormat} {esd.DarkSoulsCount} - {esd.Unk70} {esd.Unk74} {esd.Unk78} {esd.Unk7C}");

            foreach ((int, int, ESD.State) stateDesc in esd.StateGroups.SelectMany(stateGroup => stateGroup.Value.Select(state => (stateGroup.Key, state.Key, state.Value))))
            {
                (int machine, int id, ESD.State esdState) = stateDesc;
                MachineDesc eddMachine = edd.Machines.Find(m => m.ID == machine);
                State state = new State
                {
                    Machine = machine,
                    ID = id,
                    Desc = eddMachine == null ? null : eddMachine.States.Find(s => s.ID == id),
                    Inner = esdState
                };
                int targets = 0;
                if (esdState.EntryCommands.Count > 0)
                {
                    foreach (ESD.CommandCall c in esdState.EntryCommands)
                    {
                        if (c.CommandBank == 6)
                        {
                            // Console.WriteLine($"Calling {c.CommandBank} {c.CommandID}");
                            foreach (byte[] arg in c.Arguments)
                            {
                                // Console.WriteLine($"- Arg: {string.Join(" ", arg.Select(x => x.ToString("X2")))}");
                            }
                        }
                    }
                    state.Entry = EzSembler.DissembleCommandScript(ezContext, esdState.EntryCommands);
                    foreach (Statement st in state.Entry.Cmds)
                    {
                        if (st.Name.StartsWith("6:"))
                        {
                            string target = st.Name.Substring(2);
                            state.Calls.Add(int.Parse(target));
                            targets++;
                        }
                    }
                }
                if (esdState.WhileCommands.Count > 0)
                {
                    state.While = EzSembler.DissembleCommandScript(ezContext, esdState.WhileCommands);
                }
                if (esdState.ExitCommands.Count > 0)
                {
                    state.Exit = EzSembler.DissembleCommandScript(ezContext, esdState.ExitCommands);
                }
                foreach (ESD.Condition cond in esdState.Conditions)
                {
                    state.Conditions.Add(getCond(state, cond));
                }
                // Decompilation checks
                bool show = false;
                if (show) Console.Error.WriteLine(esdId + ": " + state + "\n");
                if (!machines.ContainsKey(machine)) machines[machine] = new SortedDictionary<int, State>();
                machines[machine][id] = state;
            }
            // Add reverse mapping, do some state rewriting
            // TODO: Simplify expressions for output? Probably shouldn't be done in WriteExpr itself
            foreach (SortedDictionary<int, State> states in machines.Values)
            {
                foreach (KeyValuePair<int, State> entry in states)
                {
                    int id = entry.Key;
                    State state = entry.Value;
                    foreach (int next in state.Next)
                    {
                        states[next].Prev.Add(id);
                    }
                    CollapseRegisterCalls(state);
                }
            }
            Dictionary<int, MachineArgs> machineArgs = CalculateArgs(machines);
            CalculateArgNames(machineArgs);
            // Renamed values in this block
            Dictionary<string, string> replace = new Dictionary<string, string>();
            foreach (int machine in machines.Keys)
            {
                replace[$"c6_{machine}"] = $"{esdId}_{FormatMachine(machine)}";
                MachineArgs args = machineArgs[machine];
                for (int i = 0; i < args.Count; i++)
                {
                    replace[$"c6_{machine}_{i}"] = args.Params[i].Name;
                }
            }
            // Perform decompilation per machine
            foreach (KeyValuePair<int, SortedDictionary<int, State>> machineEntry in machines.OrderBy(e => MachineSort(e.Key)))
            {
                int machine = machineEntry.Key;
                SortedDictionary<int, State> states = machineEntry.Value;

                // Print states
                // foreach (State state in states.Values) Console.WriteLine(state);

                // Redirect stdout for Python output
                TextWriter stdout = Console.Out;
                try
                {
                    if (options.Flag("cfg"))
                    {
                        CFG stateCfg = CFG.FromStates(states);
                        // stateCfg.Debug = stateCfg.Explain = true;
                        stateCfg.Classify();
                        Subtree tree = stateCfg.Structure();
                        // Make a DAG of states.
                        // If they have diamond structure, is fine. If they have multi join points, more difficult.
                        Machine m = GetProgram(machine, states, tree);

                        Console.SetOut(writer);
                        PrintProgram(esdId, m, machineArgs[machine], replace);
                    }
                    else
                    {
                        // Individual state Python
                        Machine basic = GetProgram(machine, states, null);
                        basic.Node = basic.Unused;

                        Console.SetOut(writer);
                        PrintProgram(esdId, basic, machineArgs[machine], replace);
                    }
                    Console.WriteLine();
                }
                finally
                {
                    Console.SetOut(stdout);
                }

            }
        }

        public void CollapseRegisterCalls(State state)
        {
            Dictionary<int, Expr> regs = new Dictionary<int, Expr>();
            Expr simplifyRegisters(Expr expr)
            {
                if (expr is FunctionCall f)
                {
                    if (f.Name.StartsWith("SetREG"))
                    {
                        int reg = int.Parse(f.Name.Substring(6));
                        regs[reg] = f.Args[0];
                        return f.Args[0];
                    }
                    else if (f.Name.StartsWith("GetREG"))
                    {
                        int reg = int.Parse(f.Name.Substring(6));
                        if (regs.ContainsKey(reg))
                        {
                            return regs[reg];
                        }
                    }
                }
                return null;
            }
            state.VisitConds(AstVisitor.Pre(simplifyRegisters));
        }

        public void PrintProgram(string esdId, Machine machine, MachineArgs args, Dictionary<string, string> replace)
        {
            // Also add machine names and state args
            // if (esdId == "t100100" && machine.ID == 1) PrintAst(machine.Node, 0);
            machine.Node = AnnotateStructure(machine.Node);
            string baseName = $"c6{machine.ID}";
            string machineName = FormatMachine(machine.ID);
            string funcName = replace.ContainsKey(baseName) ? replace[baseName] : $"{esdId}_{machineName}";
            IEnumerable<string> paramList = args.Params.Select((param, i) => $"{param.Name}={(param.Default == null ? "_" : param.Default.ToString())}{(i == args.Count - 1 ? "" : ",")}");
            Console.WriteLine(WordWrap($"def {funcName}", paramList.ToArray(), alwaysParens: true) + ":");
            Dictionary<string, string> subreplace = replace;
            if (args.Count > 0)
            {
                subreplace = new Dictionary<string, string>(replace);
                for (int i = 0; i < args.Count; i++)
                {
                    replace[$"arg{i}"] = args.Params[i].Name;
                }
            }
            MachineDesc eddMachine = edd.Machines.Find(m => m.ID == machine.ID);
            if (eddMachine != null && eddMachine.Name != null)
            {
                if (args.Count > 0)
                {
                    Console.WriteLine($"    \"\"\"{eddMachine.Name}");
                    for (int i = 0; i < args.Count; i++)
                    {
                        string pname = eddMachine.ParamNames[i];
                        if (pname != null)
                        {
                            Console.WriteLine($"    {args.Params[i].Name}: {pname}");
                        }
                    }
                    Console.WriteLine("    \"\"\"");
                }
                else
                {
                    string name = eddMachine.Name;
                    if (name.EndsWith("\"")) name += " ";
                    Console.WriteLine($"    \"\"\"{name}\"\"\"");
                }
            }
            PrintProgramNode(machine.Node, 1, replace, u);
        }
        public ProgramNode AnnotateStructure(ProgramNode top)
        {
            HashSet<int> loopTargets = new HashSet<int>();
            HashSet<int> gotoTargets = new HashSet<int>();
            int topLoops = 0;
            // Find all jumps, and also give a state ordering for labels
            Dictionary<int, int> stateIndex = new Dictionary<int, int>();
            void firstPass(ProgramNode node, bool inLoop)
            {
                int state = node.State;
                if (!stateIndex.ContainsKey(state)) stateIndex[state] = stateIndex.Count;
                if (node is ProgNext next)
                {
                    foreach (ProgBranch branch in next.Branches)
                    {
                        if (branch.Result != null)
                        {
                            firstPass(branch.Result, inLoop);
                        }
                    }
                }
                else if (node is ProgJump jump)
                {
                    if (jump.Type == JumpType.Goto)
                    {
                        gotoTargets.Add(jump.Target);
                    }
                    else if (!jump.LabelImplied)
                    {
                        loopTargets.Add(jump.LoopIdent);
                    }
                }
                else if (node is ProgLoop loop)
                {
                    if (!inLoop) topLoops++;
                    firstPass(loop.Node, true);
                }
                else if (node is ProgSeq seq)
                {
                    foreach (ProgramNode sub in seq.Nodes)
                    {
                        firstPass(sub, inLoop);
                    }
                }
            }
            firstPass(top, false);
            Dictionary<int, string> labels;
            if (options.Flag("cfg"))
            {
                labels = gotoTargets.OrderBy(t => stateIndex.ContainsKey(t) ? stateIndex[t] : throw new Exception($"Can't goto {t}")).Select((s, i) => (s, i)).ToDictionary(v => v.Item1, v => $"L{v.Item2}");
            }
            else
            {
                // If no CFG, just make labels the same as the state ids
                labels = gotoTargets.ToDictionary(e => e, e => $"L{e}");
            }
            Dictionary<int, string> loops = loopTargets.OrderBy(t => stateIndex.ContainsKey(t) ? stateIndex[t] : throw new Exception($"Can't goto {t}")).Select((s, i) => (s, i)).ToDictionary(v => v.Item1, v => topLoops == 1 ? (v.Item2 == 0 ? "mainloop" : $"loop{v.Item2}") : $"loop{v.Item2 + 1}");
            ProgramNode getLabel(ProgramNode node)
            {
                int state = node.State;
                if (gotoTargets.Contains(state) && !(node is ProgSeq))
                {
                    gotoTargets.Remove(state);
                    // Heuristic to add label at the start of a state, whether annotation is shown or not
                    ProgramNode label = new ProgLabel { State = state, Label = labels[state] };
                    return new ProgSeq { State = state, Nodes = node is ProgAnnotation ? new List<ProgramNode> { node, label } : new List<ProgramNode> { label, node } };
                }
                return null;
            }
            ProgramNode secondPass(ProgramNode node)
            {
                ProgramNode labelled = getLabel(node);
                if (node is ProgNext next)
                {
                    foreach (ProgBranch branch in next.Branches)
                    {
                        if (branch.Result != null)
                        {
                            ProgramNode l = secondPass(branch.Result);
                            if (l != null) branch.Result = l;
                        }
                    }
                }
                else if (node is ProgJump jump)
                {
                    if (jump.Type == JumpType.Goto)
                    {
                        jump.Label = labels[jump.Target];
                    }
                    else if (!jump.LabelImplied)
                    {
                        jump.Label = loops[jump.LoopIdent];
                    }
                }
                else if (node is ProgLoop loop)
                {
                    ProgramNode l = secondPass(loop.Node);
                    if (l != null) loop.Node = l;
                    if (loops.ContainsKey(node.State)) loop.Label = loops[node.State];
                }
                else if (node is ProgSeq seq)
                {
                    for (int i = 0; i < seq.Nodes.Count; i++)
                    {
                        ProgramNode sub = seq.Nodes[i];
                        ProgramNode l = secondPass(sub);
                        if (l != null) seq.Nodes[i] = l;
                    }
                }
                return labelled;
            }
            ProgramNode topLabel = secondPass(top);
            return topLabel == null ? top : topLabel;
        }

        public Machine GetProgram(int id, SortedDictionary<int, State> states, Subtree s)
        {
            HashSet<int> visited = new HashSet<int>();
            Machine machine = new Machine();
            machine.ID = id;
            machine.States = states;
            if (s != null) machine.Node = GetProgramNode(states, s, visited);
            Sequence unused = new Sequence();
            foreach (int node in states.Keys.Except(visited))
            {
                unused.Add(Exec.Of(node, true));
            }
            if (unused.Parts.Count > 0)
            {
                machine.Unused = GetProgramNode(states, unused.Parts.Count == 1 ? unused.Parts[0] : unused, visited);
            }
            return machine;
        }
        public ProgramNode GetProgramNode(SortedDictionary<int, State> states, Subtree s, HashSet<int> visited)
        {
            // Common funcs
            int start = s.Start();
            StateDesc desc = states[start].Desc;
            (ProgBlock, Statement, string) processBlock(Block b, List<CommandDesc> descs, string def = null, string specialCmd = null)
            {
                if (b == null) return (null, null, null);
                if (!options.Flag("cmdedd")) descs = null;
                ProgBlock pblock = new ProgBlock { State = start };
                if (def != null) pblock.Operation = def;
                Statement special = null;
                string specialName = null;
                List<string> names = new List<string>();
                for (int i = 0; i < b.Cmds.Count; i++)
                {
                    Statement st = b.Cmds[i];
                    if (special != null)
                    {
                        throw new Exception($"Special command {special} is not the last in block");
                    }
                    string name = descs != null && descs.Count > i ? descs[i].Name : null;
                    if (specialCmd != null && st.Name.StartsWith(specialCmd))
                    {
                        special = st;
                        specialName = name;
                    }
                    else
                    {
                        pblock.Add(st, name);
                    }
                }
                return (pblock, special, specialName);
            }
            ProgramNode processPassBlock(Block b)
            {
                List<ProgramNode> resNodes = new List<ProgramNode>();
                // Currently pass docs not passed through here. But returns don't have docs anyway, it seems.
                (ProgBlock passBlock, Statement ret, string retName) = processBlock(b, null, specialCmd: "7:-1");
                if (passBlock.Statements.Count > 0) resNodes.Add(passBlock);
                if (ret != null) resNodes.Add(new ProgReturn { State = start, Value = ret.Args[0].AsInt(), Doc = retName });
                if (resNodes.Count == 0) throw new Exception($"Have pass block {b} but no commands extracted");
                return ProgSeq.From(resNodes);
            }
            List<ProgramNode> processExtraBlocks(State state)
            {
                List<ProgramNode> enodes = new List<ProgramNode>();
                (ProgBlock wb, _, _) = processBlock(state.While, desc?.WhileCommands, def: "WhilePaused");
                if (wb != null) enodes.Add(wb);
                (ProgBlock eb, _, _) = processBlock(state.Exit, desc?.ExitCommands, def: "ExitPause");
                if (eb != null) enodes.Add(eb);
                return enodes;
            }
            ProgJump jumpTo(int target)
            {
                if (target == s.Next)
                {
                    return null;
                }
                JumpType type = JumpType.Goto;
                bool implied = false;
                int loopIdent = -1;
                if (s.Continues.Contains(target))
                {
                    type = JumpType.Continue;
                    implied = s.Continues.IndexOf(target) == s.Continues.Count - 1;
                    loopIdent = target;
                }
                else if (s.Breaks.Contains(target))
                {
                    type = JumpType.Break;
                    implied = s.Breaks.IndexOf(target) == s.Breaks.Count - 1;
                    loopIdent = s.Continues[s.Breaks.IndexOf(target)];
                }
                return new ProgJump { State = start, Type = type, Target = target, LabelImplied = implied, LoopIdent = loopIdent };
            }
            // Logic
            List<ProgramNode> nodes = new List<ProgramNode>();
            // For the most part, declare states as they come up, with the exception of loops - those involve
            // skipping past the 'while True' and declaring the state there, because in compilation the loop
            // state is the first visited node of the loop.
            // XX
            if (!visited.Contains(start) && !(s is Loop || s is Sequence))
            {
                ProgAnnotation ann = new ProgAnnotation { State = start, States = new List<int> { start }, StateDoc = new[] { desc?.Name }.Where(n => n != null).ToList() };
                nodes.Add(ann);
                visited.Add(start);
            }
            int next = s.Next;
            if (s is Exec e)
            {
                State state = states[e.State];
                (ProgBlock block, Statement call, string callDoc) = processBlock(state.Entry, desc?.EntryCommands, specialCmd: "6:");
                if (block != null) nodes.Add(block);
                // Print call if eligible, to end the entry block. Otherwise if the call is part of the conditions, move that down there.
                List<List<Condition>> conds = state.FlattenConds();
                // If this is not part of an if statement, there are a few cases
                // No destination: tail call or end of the line. No value returns, since those are always within transitions.
                if (conds.Count == 0)
                {
                    if (call != null)
                    {
                        block.Add(call, callDoc);
                    }
                    nodes.AddRange(processExtraBlocks(state));
                    if (next != -1)
                    {
                        nodes.Add(new ProgReturn { State = start });
                    }
                }
                // Otherwise, continuation is either unconditional, await, or goto (irreducible case).
                else
                {
                    ProgNext progNext = new ProgNext { State = start, Call = call };
                    List<ProgramNode> extras = processExtraBlocks(state);
                    if (extras.Count > 0) progNext.PreBranch = ProgSeq.From(extras);
                    foreach (List<Condition> cond in conds)
                    {
                        ProgBranch br = new ProgBranch { Cond = Condition.Combine(cond, true), CallUsages = cond.Sum(c => c.CountCallUsages()) };
                        progNext.Branches.Add(br);
                        Condition resCond = cond.Last();
                        List<ProgramNode> bnodes = new List<ProgramNode>();
                        if (resCond.Pass == null && resCond.TargetState == null) throw new Exception($"Invalid condition set {string.Join(", ", conds)}");
                        if (resCond.Pass != null)
                        {
                            ProgramNode subnode = processPassBlock(resCond.Pass);
                            if (subnode != null) bnodes.Add(subnode);
                        }
                        if (resCond.TargetState != null)
                        {
                            int target = (int)resCond.TargetState;
                            ProgramNode subnode = jumpTo(target);
                            if (subnode != null) bnodes.Add(subnode);
                            br.Target = target;
                        }
                        br.Result = bnodes.Count == 0 ? null : ProgSeq.From(bnodes);
                    }
                    if (!progNext.IsEmpty()) nodes.Add(progNext);
                }
            }
            else if (s is IfElse ie)
            {
                State state = states[ie.State];
                (ProgBlock block, Statement call, string callDoc) = processBlock(state.Entry, desc?.EntryCommands, specialCmd: "6:");
                if (block != null) nodes.Add(block);
                // Print call if eligible, to end the entry block. Otherwise if the call is part of the conditions, move that down there.
                List<List<Condition>> conds = state.FlattenConds();
                if (conds.Count < 2) throw new Exception($"If statement generated for {state} but not enough branches");
                ProgNext progNext = new ProgNext { State = start, Call = call, CallDoc = callDoc };
                nodes.Add(progNext);
                List<ProgramNode> extras = processExtraBlocks(state);
                if (extras.Count > 0) progNext.PreBranch = ProgSeq.From(extras);
                // TODO: Can combine adjacent nodes leading to the same target with or condition
                foreach (List<Condition> cond in conds)
                {
                    ProgBranch br = new ProgBranch { Cond = Condition.Combine(cond, true), CallUsages = cond.Sum(c => c.CountCallUsages()) };
                    progNext.Branches.Add(br);
                    Condition resCond = cond.Last();
                    List<ProgramNode> bnodes = new List<ProgramNode>();
                    if (resCond.Pass == null && resCond.TargetState == null) throw new Exception($"Invalid condition set {string.Join(", ", conds)}");
                    if (resCond.Pass != null)
                    {
                        ProgramNode subnode = processPassBlock(resCond.Pass);
                        if (subnode != null) bnodes.Add(subnode);
                    }
                    if (resCond.TargetState != null)
                    {
                        int target = (int)resCond.TargetState;
                        ProgramNode subnode;
                        if (ie.Branches.ContainsKey(target) && ie.Branches[target] != null && !visited.Contains(target))
                        {
                            subnode = GetProgramNode(states, ie.Branches[target], visited);
                        }
                        else
                        {
                            subnode = jumpTo(target);
                        }
                        if (subnode != null) bnodes.Add(subnode);
                        br.Target = target;
                    }
                    br.Result = bnodes.Count == 0 ? null : ProgSeq.From(bnodes);
                }
            }
            else if (s is Loop l)
            {
                ProgLoop progl = new ProgLoop { State = start };
                nodes.Add(progl);
                List<ProgramNode> lnodes = new List<ProgramNode>();
                foreach (Subtree part in l.Parts)
                {
                    ProgramNode subnode = GetProgramNode(states, part, visited);
                    if (subnode != null) lnodes.Add(subnode);
                }
                if (lnodes.Count == 0) throw new Exception("Empty loop");
                progl.Node = ProgSeq.From(lnodes);
            }
            else if (s is Sequence seq)
            {
                foreach (Subtree part in seq.Parts)
                {
                    ProgramNode subnode = GetProgramNode(states, part, visited);
                    if (subnode != null) nodes.Add(subnode);
                }
            }
            if (nodes.Count == 0) return null;
            return ProgSeq.From(nodes);
        }
        // A sequence of states which can appear in code as a lexical structure at some level of indentation.
        // Gotos can only go to starts of subtrees, or within unordered blocks.
        public abstract class Subtree
        {
            // Lexical structure info, added after initial generation, so it's not unreasonably complicated
            // The next node that executes after this one. -1 if end of program, loop head if end of loop.
            public int Next = -1;
            // All available break/continue destinations. The last one is the innermost, so does not require a label.
            public List<int> Breaks = new List<int>();
            public List<int> Continues = new List<int>();
            public abstract int Start();
        }
        public class Exec : Subtree
        {
            public int State { get; set; }
            public bool Unused { get; set; }
            public static Exec Of(int s, bool unused=false) => new Exec { State = s, Unused = unused };
            public override int Start() => State;
        }
        public class IfElse : Subtree
        {
            // The if node. Implies an Exec for that node, plus one branch per outgoing edge.
            public int State { get; set; }
            public Dictionary<int, Subtree> Branches = new Dictionary<int, Subtree>();
            public static IfElse Of(int s) => new IfElse { State = s };
            public override int Start() => State;
        }
        public class Loop : Subtree
        {
            // The loop head. Does *not* imply an Exec, as it may be nested in a conditional
            public int Head { get; set; }
            public List<Subtree> Parts = new List<Subtree>();
            public static Loop Of(int s) => new Loop { Head = s };
            public override int Start() => Head;
            public void Add(Subtree s)
            {
                if (s != null) Parts.Add(s);
            }
        }
        public class Sequence : Subtree
        {
            public List<Subtree> Parts = new List<Subtree>();
            public override int Start() => Parts[0].Start();
            public void Add(Subtree s)
            {
                if (s != null) Parts.Add(s);
            }
            public Subtree Simplify()
            {
                List<Subtree> newParts = new List<Subtree>();
                foreach (Subtree part in Parts)
                {
                    if (part is Sequence subseq)
                    {
                        Subtree subsim = subseq.Simplify();
                        if (subsim is Sequence subseqsim)
                        {
                            newParts.AddRange(subseqsim.Parts);
                        }
                        else
                        {
                            newParts.Add(subsim);
                        }
                    }
                    else
                    {
                        newParts.Add(part);
                    }
                }
                return newParts.Count == 1 ? newParts[0] : new Sequence { Parts = newParts };
            }
        }
        public static void Annotate(Subtree sub)
        {
            AnnotateRec(sub, -1, new List<int>(), new List<int>());
        }
        public static void AnnotateRec(Subtree s, int next, List<int> breaks, List<int> continues)
        {
            if (s == null) return;
            s.Breaks = breaks;
            s.Continues = continues;
            s.Next = next;
            void annotateSeq(List<Subtree> subsub, int lastNext, List<int> subbr, List<int> subcont)
            {
                for (int i = 0; i < subsub.Count; i++)
                {
                    Subtree item = subsub[i];
                    int subnext = i == subsub.Count - 1 ? lastNext : subsub[i + 1].Start();
                    AnnotateRec(item, subnext, subbr, subcont);
                }
            }
            if (s is Exec e)
            {
                // Nothing to do
            }
            else if (s is IfElse ie)
            {
                foreach (KeyValuePair<int, Subtree> branch in ie.Branches)
                {
                    AnnotateRec(branch.Value, next, breaks, continues);
                }
            }
            else if (s is Loop l)
            {
                List<int> subbr = breaks.ToList();
                List<int> subcont = continues.ToList();
                subbr.Add(next);
                subcont.Add(l.Head);
                annotateSeq(l.Parts, l.Head, subbr, subcont);
            }
            else if (s is Sequence seq)
            {
                annotateSeq(seq.Parts, next, breaks, continues);
            }
            else throw new Exception("Unknown AST type");
        }
        public class CFG
        {
            public Dictionary<int, CFGNode> Nodes { get; set; }
            public Dictionary<int, HashSet<int>> Intervals { get; set; }
            public List<int> Postorder { get; set; }
            public bool Explain { get; set; }
            public bool Debug { get; set; }
            public Subtree Structure()
            {
                // return null;
                void printStructure(Subtree s, string sp)
                {
                    if (s is Exec e)
                    {
                        Console.WriteLine($"{sp}Exec {e.State} (to {string.Join(", ", Nodes[e.State].Next)})");
                    }
                    else if (s is IfElse ie)
                    {
                        Console.WriteLine($"{sp}IfElse {ie.State} (to {string.Join(", ", Nodes[ie.State].Next)})");
                        foreach (KeyValuePair<int, Subtree> branch in ie.Branches)
                        {
                            Console.WriteLine(sp + "  " + branch.Key);
                            printStructure(branch.Value, sp + "  ");
                        }
                    }
                    else if (s is Loop l)
                    {
                        Console.WriteLine($"{sp}while True:");
                        foreach (Subtree branch in l.Parts)
                        {
                            printStructure(branch, sp + "  ");
                        }
                    }
                    else if (s is Sequence seq)
                    {
                        foreach (Subtree branch in seq.Parts)
                        {
                            printStructure(branch, sp);
                        }
                    }
                }
                Subtree sub = StructureRec(0, new List<int>(), new List<int>(), new List<int>());
                Annotate(sub);
                // printStructure(sub, "");
                return sub;
            }
            private Subtree StructureRec(int current, List<int> loops, List<int> follows, List<int> visited)
            {
                // This includes 'official' exits out of the loops, end of if/else branches
                if (follows.Contains(current)) return null; // Implicit.Of(current);
                // This includes irreducible structures and continues in loops
                if (visited.Contains(current)) return null;
                // Force breaking out of a loop within the loop
                // Revisit this...
                // if (loops.Count > 0 && (!LoopHead.ContainsKey(current) || !loops.Contains(LoopHead[current]))) return Break.Of(current);
                visited.Add(current);
                follows = follows.ToList();
                loops = loops.ToList();
                CFGNode node = Nodes[current];
                Subtree start = null;
                int followNode = current;
                List<int> standingNexts = null;
                (IfElse, int) handleCond()
                {
                    int condFollow = CondFollow[current];
                    condFollow = condFollow == END ? -1 : condFollow;
                    if (condFollow != -1) follows.Add(condFollow);
                    IfElse sub = IfElse.Of(current);
                    foreach (int next in node.Next)
                    {
                        sub.Branches[next] = StructureRec(next, loops, follows, visited);
                    }
                    if (condFollow != -1) follows.RemoveAt(follows.Count - 1);
                    return (sub, condFollow);
                }
                if (LoopFollow.ContainsKey(current))
                {
                    loops.Add(current);
                    int loopFollow = LoopFollow[current];
                    if (loopFollow != -1) follows.Add(loopFollow);
                    if (CondFollow.ContainsKey(current))
                    {
                        // If there is a loop follow and cond follow, this node should only branch into loop nodes. So all branches can be explored.
                        // Handle this being -1?
                        (IfElse ie, int condFollow) = handleCond();
                        Loop l = Loop.Of(current);
                        start = l;
                        l.Add(ie);
                        if (condFollow != -1)
                        {
                            l.Add(StructureRec(condFollow, loops, follows, visited));
                        }
                        followNode = loopFollow;
                    }
                    else
                    {
                        Loop l = Loop.Of(current);
                        start = l;
                        l.Add(Exec.Of(current));
                        // How to handle two-way branch in loop precheck node that escapes loop? break + reentry
                        // How to handle break in endless loop? - maybe it will handle itself, we'll see
                        // How to handle continue in endless loop??
                        List<int> nexts = node.Next.ToList();
                        foreach (int next in node.Next) // .Where(n => LoopHead.ContainsKey(n) && LoopHead[n] == current))
                        {
                            l.Add(StructureRec(next, loops, follows, visited));
                            nexts.Remove(next);
                        }
                        if (nexts.Count == 0)
                        {
                            // It's a break... gotta handle this...?
                            followNode = loopFollow;
                        }
                        else if (nexts.Count == 1)
                        {
                            if (nexts[0] != loopFollow) Console.WriteLine($"XXX loop follow {loopFollow} is not remaining branch {nexts[0]}");
                            followNode = loopFollow;
                        }
                        else
                        {
                            if (!nexts.Contains(loopFollow)) Console.WriteLine($"XXX loop follow {loopFollow} is not remaining branch {string.Join(", ", nexts[0])}");
                            standingNexts = nexts;
                            followNode = -1;
                        }
                    }
                    if (loopFollow != -1) follows.RemoveAt(follows.Count - 1);
                    loops.RemoveAt(loops.Count - 1);
                }
                else if (CondFollow.ContainsKey(current))
                {
                    (IfElse ie, int condFollow) = handleCond();
                    start = ie;
                    // TODO: This is necessary to solve conds at the end. happens in Kuro
                    // followNode = condFollow;
                    followNode = condFollow == current ? -1 : condFollow;
                }
                if (standingNexts != null)
                {
                    if (followNode != -1 || start == null) throw new Exception($"Standing nexts for {current} but no starting node {start} or follow node {followNode}");
                    Sequence seq = new Sequence();
                    seq.Add(start);
                    IfElse ie = IfElse.Of(current);
                    foreach (int next in standingNexts)
                    {
                        // Hm... maybe should have both in-loop conds and out-loop conds. But fuck it we'll see what this does
                        ie.Branches[next] = StructureRec(next, loops, follows, visited);
                    }
                    seq.Add(ie);
                    return seq;
                }
                else if (start != null)
                {
                    if (followNode == current) throw new Exception($"Set start node {start} but follow node is still {current}");
                    if (followNode == -1) return start;
                    Subtree next = StructureRec(followNode, loops, follows, visited);
                    Sequence seq = new Sequence();
                    seq.Add(start);
                    seq.Add(next);
                    return seq;
                }
                Subtree ret = Exec.Of(followNode);
                if (node.Next.Count == 0)
                {
                    return ret;
                }
                Sequence mseq = new Sequence();
                mseq.Add(ret);
                foreach (int next in node.Next)
                {
                    mseq.Add(StructureRec(next, loops, follows, visited));
                }
                return mseq;
            }
            public void GetCondTree()
            {
                HashSet<int> reachable = new HashSet<int>(Intervals.SelectMany(e => e.Value));
                // Console.WriteLine($"Ending nodes: {string.Join(", ", Nodes.Where(e => e.Value.Next.Count == 0 && reachable.Contains(e.Key)).Select(e => e.Key))}");
                void calcDominators(HashSet<int> doms, int forNode, int pathNode)
                {
                    if (!doms.Contains(pathNode)) return;
                    // if (forNode == pathNode) return;
                    doms.Remove(pathNode);
                    foreach (int next in Nodes[pathNode].Next)
                    {
                        calcDominators(doms, forNode, next);
                    }
                }
                Dictionary<int, HashSet<int>> dominators = reachable.ToDictionary(node => node, node => new HashSet<int>(reachable.Where(r => r != node)));
                foreach (int node in reachable)
                {
                    calcDominators(dominators[node], node, 0);
                }
                // dominators[END] = new HashSet<int>(reachable);
                Dictionary<int, HashSet<int>> immed = dominators.ToDictionary(e => e.Key, e => new HashSet<int>(e.Value));
                foreach (int node in reachable)
                {
                    foreach (int dom in dominators[node].ToList())
                    {
                        if (dominators[node].Any(dom2 => dominators[dom2].Contains(dom)))
                        {
                            immed[node].Remove(dom);
                        }
                    }
                }
                if (Debug)
                {
                    foreach (int node in reachable)
                    {
                        Console.WriteLine($"Dom {node}: [{string.Join(", ", immed[node])}]. With [{string.Join(", ", dominators[node].Intersect(Nodes[node].Next))}] direct, [{string.Join(", ", dominators[node].Except(Nodes[node].Next))}] indirect");
                    }
                }
                List<int> unresolved = new List<int>();
                foreach (int node in Postorder)
                {
                    // The original algorithm avoids adding if statements on loop conditions, but if statements are how loop conditions are implemented.
                    if (Nodes[node].Next.Count < 2) continue;
                    int startNode = node;
                    if (Nodes[node].Next.Any(next => !immed[node].Contains(next)))
                    {
                        HashSet<int> nextImmeds = new HashSet<int>(immed.Where(e => Nodes[node].Next.Intersect(e.Value).Count() > 0).Select(e => e.Key));
                        while (nextImmeds.Count > 1)
                        {
                            List<int> pair = nextImmeds.Take(2).ToList();
                            int i1 = pair[0], i2 = pair[1];
                            if (dominators[i1].Contains(i2))
                            {
                                nextImmeds.Remove(i2);
                            }
                            else if (dominators[i2].Contains(i1))
                            {
                                nextImmeds.Remove(i1);
                            }
                            else
                            {
                                throw new Exception("Have to implement LCA");
                            }
                        }
                        startNode = nextImmeds.First();
                    }
                    List<int> immeds = immed[startNode].ToList();
                    List<int> multiImmeds = immeds.Where(im => Nodes[im].Prev.Count > 1).ToList();
                    int farthestImmed = multiImmeds.OrderBy(im => Postorder.IndexOf(im)).DefaultIfEmpty(-1).First();
                    // Detect if/else within loop bodies
                    if (farthestImmed == -1 && immeds.All(im => LoopHead.ContainsKey(im)) && immeds.Select(im => LoopHead[im]).Distinct().Count() == 1)
                    {
                        farthestImmed = END;
                    }
                    // Detect branches which both exit the current machine
                    if (farthestImmed == -1 && immed[startNode].All(im => Nodes[im].End.Count == 1)) farthestImmed = END;
                    if (Debug) Console.WriteLine($"For {Nodes[node].Next.Count}-way node {node} with {string.Join(",", immed[startNode])}, they merge back into {string.Join(",", multiImmeds)}, chosen {farthestImmed}");
                    if (farthestImmed == -1)
                    {
                        unresolved.Add(node);
                    }
                    else
                    {
                        CondFollow[node] = farthestImmed;
                        foreach (int otherFollow in unresolved) CondFollow[otherFollow] = farthestImmed;
                        if (Explain) Console.WriteLine($"If/else join for main node {node} + nested nodes [{string.Join(", ", unresolved)}] -> {farthestImmed}");
                        unresolved.Clear();
                    }
                }
            }
            public Dictionary<int, int> LoopHead = new Dictionary<int, int>();
            public Dictionary<int, List<int>> LoopLatch = new Dictionary<int, List<int>>();
            public Dictionary<int, int> CondFollow = new Dictionary<int, int>();
            public Dictionary<int, int> LoopFollow = new Dictionary<int, int>();
            public Dictionary<int, LoopType> LoopTypes = new Dictionary<int, LoopType>();
            public enum LoopType
            {
                // Used mainly to determine what best follow node is
                PRECHECK, POSTCHECK, NOCHECK
            }
            public void Classify()
            {
                // Add terminal conditions for returns and tail calls
                foreach (CFGNode node in Nodes.Values)
                {
                    if (node.Next.Count == 0) node.End.Add(END);
                }
                GetAllBackedges();
                // Backpropagate end tags to minimize unnecessary gotos. (To check: is this still used?)
                int added = 0;
                do
                {
                    added = 0;
                    foreach (KeyValuePair<int, CFGNode> entry in Nodes)
                    {
                        CFGNode node = entry.Value;
                        if (node.End.Count == 1)
                        {
                            foreach (int prev in node.Prev)
                            {
                                CFGNode prevNode = Nodes[prev];
                                if (prevNode.End.Count == 0 && prevNode.Next.Count == 1 && prevNode.Next.First() == entry.Key)
                                {
                                    prevNode.End.Add(END);
                                    added++;
                                }
                            }
                        }
                    }
                } while (added != 0);
                GetCondTree();
            }
            private void GetAllBackedges()
            {
                GetBackedges();
                CFG sub = GetIntervalGraph();
                if (sub != null)
                {
                    sub.GetAllBackedges();
                    if (Debug) Console.WriteLine($"Exiting recursion; sub has {sub.LoopHead.Count} heads and {sub.LoopLatch.Count} latches");
                    foreach (KeyValuePair<int, List<int>> entry in sub.LoopLatch)
                    {
                        HashSet<int> fromValues = Intervals[entry.Key];
                        foreach (int h in entry.Value)
                        {
                            List<int> latches = Nodes[h].Prev.Where(p => fromValues.Contains(p)).ToList();
                            List<int> headersInLoop = sub.LoopHead.Where(e => e.Value == h).Select(e => e.Key).ToList();
                            HashSet<int> intervalsInLoop = new HashSet<int>(Intervals.Where(e => headersInLoop.Contains(e.Key)).SelectMany(e => e.Value));
                            if (Debug) Console.WriteLine($"For higher level backedge {string.Join(",", entry.Value)}->{entry.Key}, prevs are {string.Join(",", Nodes[h].Prev)} latches are {string.Join(", ", latches)}");
                            foreach (int latch in latches)
                            {
                                AddLatch(h, latch, intervalsInLoop);
                            }
                        }
                    }
                }
            }
            public void AddLatch(int h, int latch, HashSet<int> interval)
            {
                AddMulti(LoopLatch, latch, h);
                // Find nodes in loop h -> latch -> h
                int headIndex = Postorder.IndexOf(h);
                int latchIndex = Postorder.IndexOf(latch);
                if (headIndex == -1 || latchIndex == -1) throw new Exception("Unreachable loop nodes");
                if (Explain || Debug) Console.WriteLine($"Loop starting at head {h} (i={headIndex}) to latch {latch} (i={latchIndex})");
                LoopHead[h] = h;
                HashSet<int> inLoop = new HashSet<int>();
                for (int i = latchIndex; i <= headIndex; i++)
                {
                    int node = Postorder[i];
                    if (interval.Contains(node))
                    {
                        inLoop.Add(node);
                        if (!LoopHead.ContainsKey(node)) LoopHead[node] = h;
                    }
                }
                // Find follow node
                if (!LoopFollow.ContainsKey(h))
                {
                    LoopType type;
                    if (Nodes[h].Next.Any(next => !inLoop.Contains(next)))
                    {
                        type = LoopType.PRECHECK;
                    }
                    else
                    {
                        type = Nodes[latch].Next.Any(next => !inLoop.Contains(next)) ? LoopType.POSTCHECK : LoopType.NOCHECK;
                    }
                    LoopTypes[h] = type;
                    List<int> follows;
                    if (type == LoopType.PRECHECK)
                    {
                        follows = Nodes[h].Next.Where(next => !inLoop.Contains(next)).ToList();
                    }
                    else if (type == LoopType.POSTCHECK)
                    {
                        follows = Nodes[latch].Next.Where(next => !inLoop.Contains(next)).ToList();
                    }
                    else
                    {
                        // for all nodes in the loop with multiple exits, if any of those are not in the loop, use their nonloop exit. pick the highest postorder
                        follows = inLoop.SelectMany(loopNode => Nodes[loopNode].Next.Where(next => !inLoop.Contains(next))).ToList();
                    }
                    int follow;
                    if (follows.Count == 0)
                    {
                        if (type != LoopType.NOCHECK) throw new Exception($"No follow node found for {type} loop");
                        follow = -1;
                    }
                    else
                    {
                        follow = follows.OrderBy(cand => Postorder.IndexOf(cand)).Last();
                    }
                    if (Explain || Debug) Console.WriteLine($"Loop type {type}, with possible follows [{string.Join(", ", follows)}]. Selected {follow}");
                    LoopFollow[h] = follow;
                    // Add terminal conditions for loops
                    List<int> terminal = new List<int> { h, follow };
                    foreach (int n in inLoop)
                    {
                        HashSet<int> excl = new HashSet<int>(Nodes[n].Next.Except(terminal));
                        if (excl.Count != Nodes[n].Next.Count)
                        {
                            excl.Add(END);
                            Nodes[n].End = excl;
                        }
                    }
                }
            }
            public void GetBackedges()
            {
                if (Debug) foreach (KeyValuePair<int, HashSet<int>> e in Intervals) Console.WriteLine($"Interval {e.Key}: {string.Join(", ", e.Value)}");
                foreach (KeyValuePair<int, HashSet<int>> entry in Intervals)
                {
                    int h = entry.Key;
                    HashSet<int> interval = entry.Value;
                    List<int> latches = Nodes[h].Prev.Where(p => interval.Contains(p)).OrderBy(p => Postorder.IndexOf(p)).ToList();
                    if (Debug) Console.WriteLine($"For {entry.Key}, prevs are {string.Join(",", Nodes[h].Prev)}; latches are {string.Join(", ", latches)}");
                    foreach (int latch in latches)
                    {
                        AddLatch(h, latch, interval);
                    }
                }
            }
            public List<int> GetPostorder()
            {
                List<int> order = new List<int>();
                HashSet<int> visited = new HashSet<int>();
                void visit(int n)
                {
                    visited.Add(n);
                    foreach (int next in Nodes[n].Next)
                    {
                        if (!visited.Contains(next))
                        {
                            visit(next);
                        }
                    }
                    order.Add(n);
                }
                visit(0);
                return order;
            }
            public static CFG FromStates(SortedDictionary<int, State> states)
            {
                CFG cfg = new CFG();
                cfg.Nodes = states.Keys.ToDictionary(i => i, i => new CFGNode());
                foreach (State state in states.Values)
                {
                    foreach (int next in state.Next)
                    {
                        cfg.Nodes[state.ID].Next.Add(next);
                        cfg.Nodes[next].Prev.Add(state.ID);
                    }
                }
                cfg.AddGraphData();
                return cfg;
            }
            public CFG GetIntervalGraph()
            {
                if (Intervals.Count == Nodes.Count || Intervals.Values.All(i => i.Count == 1)) return null;
                CFG cfg = new CFG();
                cfg.Debug = Debug;
                cfg.Nodes = Intervals.Keys.ToDictionary(i => i, i => new CFGNode());
                // Map from nodes in this graph to which header node they belong do
                Dictionary<int, int> header = Intervals.SelectMany(e => e.Value.Select(i => (i, e.Key))).ToDictionary(i => i.Item1, i => i.Item2);
                foreach (KeyValuePair<int, CFGNode> entry in Nodes)
                {
                    if (!header.ContainsKey(entry.Key))
                    {
                        continue;
                    }
                    int h1 = header[entry.Key];
                    CFGNode hnode = cfg.Nodes[h1];
                    hnode.Next.UnionWith(entry.Value.Next.Select(n => header[n]).Where(h => h != h1));
                }
                foreach (KeyValuePair<int, CFGNode> entry in cfg.Nodes) foreach (int next in entry.Value.Next) cfg.Nodes[next].Prev.Add(entry.Key);
                cfg.AddGraphData();
                return cfg;
            }
            public void AddGraphData()
            {
                Intervals = GetIntervals();
                Postorder = GetPostorder();
            }
            private Dictionary<int, HashSet<int>> GetIntervals()
            {
                Dictionary<int, HashSet<int>> intervals = new Dictionary<int, HashSet<int>>();
                HashSet<int> headers = new HashSet<int> { 0 };
                HashSet<int> processed = new HashSet<int>();
                while (headers.Count > 0)
                {
                    int h = headers.First();
                    headers.Remove(h);
                    // Console.WriteLine($"Processing header {h}");
                    HashSet<int> interval = intervals[h] = new HashSet<int> { h };
                    int lastCount = 0;
                    while (lastCount != interval.Count)
                    {
                        lastCount = interval.Count;
                        foreach (int start in interval.ToList())
                        {
                            foreach (int cand in Nodes[start].Next)
                            {
                                if (Nodes[cand].Prev.All(n => interval.Contains(n)) && !intervals.ContainsKey(cand))
                                {
                                    interval.Add(cand);
                                }
                            }
                        }
                    }
                    foreach (int cand in interval)
                    {
                        // Console.WriteLine($"  Adding candidate {cand}, with nexts {string.Join(",", Nodes[cand].Next)}, except cur interval {string.Join(",", interval)} and existing headers {string.Join(",", intervals.Keys)}");
                        headers.UnionWith(Nodes[cand].Next.Except(interval).Except(intervals.Keys));
                    }
                }
                return intervals;
            }
        }
        private const int END = 9999999;
        public class CFGNode
        {
            public HashSet<int> Prev = new HashSet<int>();
            public HashSet<int> Next = new HashSet<int>();
            // To be used for dominator calculations, as these benefit from having universal end nodes
            public HashSet<int> End = new HashSet<int>();
        }

        // All of the argument logic. Not used by DS1.
        public Dictionary<int, MachineArgs> CalculateArgs(SortedDictionary<int, SortedDictionary<int, State>> machines)
        {
            Dictionary<int, MachineArgs> machineArgs = machines.Keys.ToDictionary(k => k, k => new MachineArgs { ID = k });
            Dictionary<int, HashSet<int>> usedArgs = new Dictionary<int, HashSet<int>>();
            foreach (KeyValuePair<int, SortedDictionary<int, State>> machineEntry in machines)
            {
                int machineID = machineEntry.Key;
                // Find callers and value usages
                void identifyArgs(Expr expr)
                {
                    if (expr is FunctionCall func)
                    {
                        if (func.Name == "StateGroupArg")
                        {
                            AddMulti(usedArgs, machineID, func.Args[0].AsInt());
                        }
                    }
                }
                foreach (State state in machineEntry.Value.Values)
                {
                    state.Visit(AstVisitor.PreAct(identifyArgs));
                    if (state.Entry == null) continue;
                    foreach (Statement st in state.Entry.Cmds)
                    {
                        if (st.Name.StartsWith("6:"))
                        {
                            int target = int.Parse(st.Name.Substring(2));
                            AddMulti(machineArgs[target].Callers, machineID, st);
                        }
                    }
                }
            }
            // Find all counts
            foreach (int machine in machines.Keys)
            {
                MachineArgs args = machineArgs[machine];
                HashSet<int> callerCounts = new HashSet<int>();
                foreach (Statement call in args.Callers.SelectMany(c => c.Value))
                {
                    callerCounts.Add(call.Args.Count);
                }
                int maxObserved = usedArgs.ContainsKey(args.ID) ? Enumerable.Max(usedArgs[args.ID].DefaultIfEmpty(-1)) : -1;
                int count;
                if (callerCounts.Count == 0)
                {
                    count = maxObserved == -1 ? 0 : maxObserved + 1;
                }
                else if (callerCounts.Count == 1)
                {
                    count = callerCounts.First();
                    if (maxObserved >= count) throw new Exception($"Arg {maxObserved} used in machine {esdId}-{args.ID} but callers only provide {count}");
                }
                else throw new Exception($"Inconsistent caller argument counts {string.Join(", ", callerCounts)} for machine {esdId}-{args.ID}");
                args.Count = count;
                for (int i = 0; i < count; i++)
                {
                    args.Values.Add(new List<ValueSource>());
                }
            }

            // Calculate all usages
            Dictionary<string, List<IdExtractor>> extractors = EsdExtractors();
            int? exprArg(Expr expr)
            {
                if (expr is FunctionCall func && func.Name == "StateGroupArg")
                {
                    return func.Args[0].AsInt();
                }
                return null;
            }
            foreach (MachineArgs args in machineArgs.Values)
            {
                int machineID = args.ID;
                void addUsage(string name, IdExtractor extractor, List<Expr> exprs)
                {
                    ValueUsage usage = new ValueUsage
                    {
                        Exprs = exprs.Where((arg, i) => extractor.Indices.Contains(i)).ToList(),
                        Extractor = extractor,
                    };
                    // Classify special id as concrete value, add it to arg usages, or neither
                    SortedSet<int> usageArgs = new SortedSet<int>();
                    void addArgs(Expr e2)
                    {
                        int? arg = exprArg(e2);
                        if (arg != null) usageArgs.Add((int)arg);
                    }
                    foreach (Expr e in usage.Exprs)
                    {
                        e.Visit(AstVisitor.PreAct(addArgs));
                    }
                    usage.Args = usageArgs.ToList();
                    if (usageArgs.Count == 0)
                    {
                        // TODO: Can probably move this later, once all info is available. No need to do it now
                        List<int> argValues = new List<int>();
                        foreach (Expr e in usage.Exprs)
                        {
                            if (TryEvalInt(e, out int val))
                            {
                                argValues.Add(val);
                            }
                        }
                        if (argValues.Count == usage.Exprs.Count && argValues.Count == usage.Extractor.Indices.Count)
                        {
                            Obj obj = extractor.Extract(argValues);
                            if (obj == null) return;
                            // Constant usage, the exact expr used doesn't matter, since it's always used inline
                            Expr lastExpr = usage.Exprs[usage.Exprs.Count - 1];
                            ValueSource source = (ValueSource)lastExpr.SourceInfo;
                            if (source == null)
                            {
                                lastExpr.SourceInfo = source = new ValueSource { Value = new ConstExpr { Value = argValues.Last() }, Source = lastExpr };
                            }
                            AddMulti(source.Usages, usage, obj);
                        }
                    }
                    else
                    {
                        args.Usages.Add(usage);
                    }
                }
                void identifyFuncs(Expr expr)
                {
                    if (expr is FunctionCall func)
                    {
                        if (extractors.ContainsKey(func.Name))
                        {
                            foreach (IdExtractor extractor in extractors[func.Name])
                            {
                                addUsage(func.Name, extractor, func.Args);
                            }
                        }
                    }
                    else if (expr is BinaryExpr be)
                    {
                        int? arg1 = exprArg(be.Lhs);
                        int? arg2 = exprArg(be.Rhs);
                        if (arg1 != null)
                        {
                            args.Usages.Add(new ValueUsage { Check = true, Args = new List<int> { (int)arg1 } });
                        }
                        if (arg2 != null)
                        {
                            args.Usages.Add(new ValueUsage { Check = true, Args = new List<int> { (int)arg2 } });
                        }
                    }
                }
                void identifyCmds(Statement st)
                {
                    if (!extractors.ContainsKey(st.Name)) return;
                    foreach (IdExtractor extractor in extractors[st.Name])
                    {
                        addUsage(st.Name, extractor, st.Args);
                    }
                }
                foreach (State state in machines[args.ID].Values)
                {
                    AstVisitor visitor = AstVisitor.PreAct(identifyFuncs);
                    visitor.PrevisitSt = identifyCmds;
                    state.Visit(visitor);
                }
            }
            // Fill in all arg sources.
            // This adds two annotations per value: one where the value comes from, and one where the arg is used, if unique in that context
            HashSet<int> visitedForArgs = new HashSet<int>();
            void calculateArgs(int id)
            {
                if (visitedForArgs.Contains(id)) return;
                visitedForArgs.Add(id);
                MachineArgs args = machineArgs[id];
                Dictionary<ValueUsage, Dictionary<Obj, ValueSource>> usagesForComments = new Dictionary<ValueUsage, Dictionary<Obj, ValueSource>>();
                foreach (KeyValuePair<int, List<Statement>> callerEntry in args.Callers)
                {
                    int caller = callerEntry.Key;
                    MachineArgs cargs = machineArgs[caller];
                    foreach (Statement st in callerEntry.Value)
                    {
                        Dictionary<int, int> mapping = new Dictionary<int, int>();
                        Dictionary<int, List<ValueSource>> values = new Dictionary<int, List<ValueSource>>();
                        for (int i = 0; i < st.Args.Count; i++)
                        {
                            Expr arg = st.Args[i];
                            if (arg is ConstExpr c)
                            {
                                ValueSource source = (ValueSource)c.SourceInfo;
                                if (source != null) throw new Exception($"Internal error - {esdId}-{caller} calling {id} arg source processed");
                                ValueSource newSource = new ValueSource { Value = c, Source = c };
                                c.SourceInfo = newSource;
                                AddMulti(values, i, newSource);
                            }
                            else if (arg is FunctionCall f && f.Name.Equals("StateGroupArg"))
                            {
                                mapping[i] = f.Args[0].AsInt();
                            }
                            // This is not true anymore in DS2 ai files.
                            // TODO: Check that this doesn't result in any strange behavior.
                            // else throw new Exception($"Machine arg should either be constant value or other argument - found {arg} in {esdId}-{caller} calling {id} - needs special handling");
                        }
                        if (mapping.Count != 0)
                        {
                            bool hadBefore = visitedForArgs.Contains(caller);
                            calculateArgs(caller);
                            foreach (KeyValuePair<int, int> entry in mapping)
                            {
                                AddMulti(values, entry.Key, cargs.Values[entry.Value]);
                            }
                        }
                        foreach (ValueUsage usage in args.Usages)
                        {
                            if (!usagesForComments.ContainsKey(usage)) usagesForComments[usage] = new Dictionary<Obj, ValueSource>();
                            // Just in case any used args unknown - need all of them to determine what value is
                            if (usage.Args.Any(i => !values.ContainsKey(i))) continue;
                            Dictionary<Obj, ValueSource> objsForComments = new Dictionary<Obj, ValueSource>();
                            foreach (List<ValueSource> sourceInstance in MultiCartesian(usage.Args.Select(i => values[i]).ToList()))
                            {
                                if (usage.Check)
                                {
                                    // Just add it with empty list if not used with game object.
                                    // There should probably only be one used arg in the check case.
                                    foreach (ValueSource source in sourceInstance)
                                    {
                                        if (!source.Usages.ContainsKey(usage)) source.Usages[usage] = new List<Obj>();
                                    }
                                    continue;
                                }
                                // If all sources can be used as int, eligible for usage annotation
                                Dictionary<int, int> valueMap = new Dictionary<int, int>();
                                for (int i = 0; i < sourceInstance.Count; i++)
                                {
                                    if (sourceInstance[i].Value.TryAsInt(out int sourceVal))
                                    {
                                        valueMap[usage.Args[i]] = sourceVal;
                                    }
                                }
                                if (valueMap.Count != usage.Args.Count) continue;
                                List<int> argValues = new List<int>();
                                foreach (Expr e in usage.Exprs)
                                {
                                    if (TryEvalInt(e, out int usageValue, valueMap))
                                    {
                                        argValues.Add(usageValue);
                                    }
                                }
                                if (argValues.Count != usage.Exprs.Count || argValues.Count != usage.Extractor.Indices.Count) continue;
                                Obj obj = usage.Extractor.Extract(argValues);
                                if (obj == null) continue;
                                foreach (ValueSource source in sourceInstance)
                                {
                                    AddMulti(source.Usages, usage, obj);
                                }
                                usagesForComments[usage][obj] = sourceInstance.Last();
                            }
                        }
                        foreach (KeyValuePair<int, List<ValueSource>> entry in values)
                        {
                            args.Values[entry.Key].AddRange(entry.Value);
                        }
                    }
                }
                foreach (KeyValuePair<ValueUsage, Dictionary<Obj, ValueSource>> usageEntry in usagesForComments.Where(e => e.Key.Exprs.Count > 0 && e.Value.Count == 1))
                {
                    ValueUsage usage = usageEntry.Key;
                    KeyValuePair<Obj, ValueSource> entry = usageEntry.Value.First();
                    Expr mainExpr = usage.Exprs.Last();
                    ValueSource main;
                    if (mainExpr.SourceInfo != null)
                    {
                        main = (ValueSource)mainExpr.SourceInfo;
                    }
                    else
                    {
                        main = new ValueSource { Source = entry.Value.Source, Value = entry.Value.Value, Usages = new Dictionary<ValueUsage, List<Obj>>() };
                        mainExpr.SourceInfo = main;
                        AddMulti(main.Usages, usage, entry.Key);
                    }
                }
            }
            // Calculate all immediate sites feeding into it
            // Then, calculate all transitive sites feeding into it. Evaluate constant expressions where possible.
            foreach (int machine in machineArgs.Keys)
            {
                calculateArgs(machine);
            }
            return machineArgs;
        }

        public void CalculateArgNames(Dictionary<int, MachineArgs> machineArgs)
        {
            Dictionary<string, int> argPrefixCounts = new Dictionary<string, int>();
            string nextArgName(string prefix)
            {
                if (!argPrefixCounts.ContainsKey(prefix)) argPrefixCounts[prefix] = 0;
                argPrefixCounts[prefix]++;
                return $"{prefix}{argPrefixCounts[prefix]}";
            }
            string classifyArg(List<ValueSource> sources)
            {
                List<ValueUsage> usages = sources.SelectMany(s => s.Usages.Keys).ToList();
                if (usages.Count == 0) return "z";
                if (usages.All(u => u.Check))
                {
                    if (sources.All(v => v.Value.TryAsInt(out int val) && (val == 0 || val == 1))) return "mode";
                    return "val";
                }
                Namespace ns = Namespace.GLOBAL;
                // Namespaces for objects which are concretely referenced
                HashSet<Namespace> useNamespaces = new HashSet<Namespace>(sources.SelectMany(s => s.Usages.Values.SelectMany(os => os.Select(o => o.Type))));
                // Namespaces for declared types. May differ from usages e.g. for all items vs concrete item categories
                HashSet<Namespace> declNamespaces = new HashSet<Namespace>(sources.SelectMany(s => s.Usages.Keys.Where(u => u.Extractor != null).Select(u => u.Extractor.Type)));
                if (useNamespaces.Count == 0) ns = declNamespaces.FirstOrDefault();
                else if (useNamespaces.Count == 1) ns = useNamespaces.First();
                else ns = declNamespaces.First();
                switch (ns)
                {
                    case Namespace.GLOBAL: return "z";
                    case Namespace.PROTECTOR: return "armor";
                    case Namespace.ACCESSORY: return "ring";
                    case Namespace.EVENT_FLAG: return "flag";
                    case Namespace.TALK: return "text";
                    default: return ns.ToString().ToLower();
                }
            }
            Dictionary<int, Dictionary<ValueSource, string>> allVarNames = new Dictionary<int, Dictionary<ValueSource, string>>();
            void calculateArgNames(int machine)
            {
                if (allVarNames.ContainsKey(machine)) return;
                MachineArgs args = machineArgs[machine];
                Dictionary<ValueSource, string> varNames = allVarNames[machine] = new Dictionary<ValueSource, string>();
                // Calculate all callers first
                foreach (int caller in args.Callers.Keys)
                {
                    calculateArgNames(caller);
                }
                // At the top level, there should be no args. Then basically postorder DFS from there.
                // Console.WriteLine($"# TTT {formatMachine(machine)}");
                HashSet<string> usedNames = new HashSet<string>();
                for (int i = 0; i < args.Count; i++)
                {
                    // Where did this arg come from?
                    List<ValueSource> sources = args.Values[i];
                    CommandParam param;
                    if (sources.Count == 0)
                    {
                        // Should only happen if this machine uses args but no one calls it. Just make up args
                        // Console.WriteLine($"#    ZZZ {i}");
                        // Is this possible..?
                        param = new CommandParam { Name = nextArgName("z"), Index = i };
                    }
                    else
                    {
                        // Figure out if usages already exist as arg in parents - if so, just copy the name from one of those source arg names which have not been taken here.
                        string argName = null;
                        foreach (int caller in args.Callers.Keys)
                        {
                            Dictionary<ValueSource, string> parentNames = allVarNames[caller];
                            foreach (ValueSource source in sources)
                            {
                                if (parentNames.TryGetValue(source, out string name) && !usedNames.Contains(name))
                                {
                                    argName = name;
                                    varNames[source] = name;
                                    usedNames.Add(name);
                                    break;
                                }
                            }
                            if (argName != null) break;
                        }
                        if (argName == null)
                        {
                            argName = nextArgName(classifyArg(sources));
                        }
                        HashSet<object> sourceValues = new HashSet<object>();
                        foreach (ValueSource source in sources)
                        {
                            sourceValues.Add(source.Value.Value);
                            if (!varNames.ContainsKey(source))
                            {
                                varNames[source] = argName;
                            }
                        }
                        param = new CommandParam { Name = argName, Index = i };
                        if (sourceValues.Count == 1)
                        {
                            param.Default = sourceValues.First();
                        }
                        // If it does not exist as args in parent, it must have been a literal in the parent. In that case, create a name.
                        // Console.WriteLine($"#    {i}: {string.Join("; ", values.Select(v => $"{v.Value}[{string.Join(" - ", v.Usages.Values.Select(os => string.Join(", ", os)))}]"))}");
                        // ValueSource main = values.OrderBy(v => v.Usages.Values.Select(o => o.Count).Sum())
                    }
                    args.Params.Add(param);
                    // Console.WriteLine($"#   {i}: {param.Name}={param.Default}");
                }
            }
            foreach (int machine in machineArgs.Keys)
            {
                calculateArgNames(machine);
            }
        }

        private Dictionary<string, List<IdExtractor>> EsdExtractors()
        {
            // For now, hardcode these. No args are yet 'checked' outside of this.
            Dictionary<string, List<IdExtractor>> extractors = new Dictionary<string, List<IdExtractor>>();
            // Functions
            AddMulti(extractors, "ComparePlayerInventoryNumber", new IdExtractor
            {
                Indices = new List<int> { 0, 1 },
                Extract = args => Obj.Item((uint)args[0], args[1]),
                Type = Namespace.ITEM,
            });
            AddMulti(extractors, "IsEquipmentIDObtained", extractors["ComparePlayerInventoryNumber"][0]);
            AddMulti(extractors, "GetEventStatus", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.EventFlag(args[0]),
                Type = Namespace.EVENT_FLAG,
            });
            AddMulti(extractors, "TalkToPlayer", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Talk(args[0]),
                Type = Namespace.TALK,
            });
            AddMulti(extractors, "TalkToPlayer", new IdExtractor
            {
                Indices = new List<int> { 3 },
                Extract = args => args.Count == 0 || args[0] == -1 ? null : Obj.EventFlag(args[0]),
                Type = Namespace.EVENT_FLAG,
            });
            // Commands
            AddMulti(extractors, "GetEventState", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.EventFlag(args[0]),
                Type = Namespace.EVENT_FLAG,
            });
            AddMulti(extractors, "OpenRegularShop", new IdExtractor
            {
                Indices = new List<int> { 0, 1 },
                Extract = args => Obj.Shop(args[0], args[1]),
                Type = Namespace.SHOP,
            });
            AddMulti(extractors, "AddTalkListData", new IdExtractor
            {
                Indices = new List<int> { 1 },
                Extract = args => Obj.Action(args[0]),
                Type = Namespace.ACTION,
            });
            AddMulti(extractors, "OpenGenericDialog", extractors["AddTalkListData"][0]);
            AddMulti(extractors, "AddTalkListData", new IdExtractor
            {
                Indices = new List<int> { 2 },
                Extract = args => args[0] == -1 ? null : Obj.EventFlag(args[0]),
                Type = Namespace.EVENT_FLAG,
            });
            AddMulti(extractors, "AddTalkListDataIf", new IdExtractor
            {
                Indices = new List<int> { 2 },
                Extract = args => Obj.Action(args[0]),
                Type = Namespace.ACTION,
            });
            AddMulti(extractors, "DisplayOneLineHelp", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Action(args[0]),
                Type = Namespace.ACTION,
            });
            AddMulti(extractors, "GetItemFromItemLot", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Lot(args[0]),
                Type = Namespace.LOT,
            });
            AddMulti(extractors, "PlayerEquipmentQuantityChange", new IdExtractor
            {
                Indices = new List<int> { 0, 1 },
                Extract = args => Obj.Item((uint)args[0], args[1]),
                Type = Namespace.ITEM,
            });
            AddMulti(extractors, "GetItemHeldNumLimit", extractors["PlayerEquipmentQuantityChange"][0]);
            AddMulti(extractors, "ReplaceTool", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Item(3, args[0]),
                Type = Namespace.GOODS,
            });
            AddMulti(extractors, "ReplaceTool", new IdExtractor
            {
                Indices = new List<int> { 1 },
                Extract = args => Obj.Item(3, args[0]),
                Type = Namespace.GOODS,
            });
            // DS2
            IdExtractor messageExtractor = new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Action(args[0]),
                Type = Namespace.ACTION
            };
            AddMulti(extractors, "DisplayOwnYesNoMenu", messageExtractor);
            AddMulti(extractors, "DisplayYesNoMenu", messageExtractor);
            AddMulti(extractors, "DisplayOwnOkMenu", messageExtractor);
            AddMulti(extractors, "DisplayOkMenu", messageExtractor);
            AddMulti(extractors, "DisplayEventMessage", messageExtractor);

            IdExtractor messageItemExtractor(int index) => new IdExtractor
            {
                Indices = new List<int> { index, index + 1 },
                Extract = args => args[0] == 2 && args[1] != 0 ? Obj.Item(3, args[1]) : null,
                Type = Namespace.GOODS,
            };
            AddMulti(extractors, "DisplayOwnYesNoMenu", messageItemExtractor(3));
            AddMulti(extractors, "DisplayYesNoMenu", messageItemExtractor(4));
            AddMulti(extractors, "DisplayOwnOkMenu", messageItemExtractor(4));
            AddMulti(extractors, "DisplayOkMenu", messageItemExtractor(5));

            IdExtractor dialogueExtractor = new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Talk(args[0]),
                Type = Namespace.TALK
            };
            AddMulti(extractors, "StartConversation", dialogueExtractor);
            AddMulti(extractors, "ShowYesNoSelection", messageExtractor);

            IdExtractor itemExtractor(int index, bool lot) => new IdExtractor
            {
                Indices = new List<int> { index },
                Extract = args => lot ? Obj.Lot(args[0]) : Obj.Item(3, args[0]),
                Type = lot ? Namespace.LOT : Namespace.GOODS,
            };
            AddMulti(extractors, "ConsumeItem", itemExtractor(0, false));
            AddMulti(extractors, "AwardItem", itemExtractor(0, true));
            AddMulti(extractors, "DoesPlayerHaveItem", itemExtractor(1, false));
            AddMulti(extractors, "IsItemEquipped", itemExtractor(1, false));
            AddMulti(extractors, "IsItemLeft", itemExtractor(1, false));
            AddMulti(extractors, "DisplayItemAwardFailure", itemExtractor(0, true));
            // DS2 functions
            AddMulti(extractors, "ItemCount", itemExtractor(0, false));
            AddMulti(extractors, "CanGetItem", itemExtractor(0, false));
            AddMulti(extractors, "EquippedItemCount", itemExtractor(0, false));
            AddMulti(extractors, "CanGetItemLot", itemExtractor(0, true));
            AddMulti(extractors, "NpcParamTextId", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Npc(args[0]),
                Type = Namespace.NPC
            });
            AddMulti(extractors, "CompareGameCycleForBonfire", new IdExtractor
            {
                Indices = new List<int> { 1 },
                Extract = args => Obj.Bonfire(args[0]),
                Type = Namespace.BONFIRE
            });
            AddMulti(extractors, "GetBonfireAsceticCount", new IdExtractor
            {
                Indices = new List<int> { 0 },
                Extract = args => Obj.Bonfire(args[0]),
                Type = Namespace.BONFIRE
            });

            return extractors;
        }
    }
}
