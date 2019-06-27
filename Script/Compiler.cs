using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using Microsoft.Scripting.Hosting.Providers;
using Microsoft.Scripting.Runtime;
using Microsoft.Scripting.Utils;

using IronPython;
using IronPython.Compiler;
using IronPython.Runtime;
using Py = IronPython.Compiler.Ast;

using ESDLang.EzSemble;
using SoulsFormats;

using static ESDLang.EzSemble.AST;
using static ESDLang.Script.Common;

namespace ESDLang.Script
{
    public class Compiler
    {
        private readonly EzSembleContext ezContext;
        private readonly ESDOptions options;
        public Compiler(EzSembleContext ezContext, ESDOptions options)
        {
            this.ezContext = ezContext;
            this.options = options;
        }

        public Dictionary<string, ESD> Compile(string path, ESD baseESD, Predicate<string> esdFilter=null)
        {
            ScriptRuntimeSetup setup = new ScriptRuntimeSetup();
            setup.LanguageSetups.Add(IronPython.Hosting.Python.CreateLanguageSetup(null));
            ScriptRuntime runtime = new ScriptRuntime(setup);
            ScriptDomainManager domain = HostingHelpers.GetDomainManager(runtime);
            PythonContext pyContext = new PythonContext(domain, null);
            CodeContext codeContext = new CodeContext(new PythonDictionary(), new ModuleContext(new PythonDictionary(), DefaultContext.DefaultPythonContext));
            SourceUnit sourceUnit = codeContext.LanguageContext.CreateFileUnit(path);
            Parser parser = Parser.CreateParser(
                new CompilerContext(sourceUnit, new PythonCompilerOptions(), ErrorSink.Default),
                (PythonOptions)codeContext.LanguageContext.Options);
            Py.PythonAst ast;
            try
            {
                ast = parser.ParseFile(false);
            }
            catch (SyntaxErrorException ex)
            {
                Console.WriteLine($"ERROR: {ex.Message}");
                Console.WriteLine($"{ex.SourcePath}:{ex.Line}:{ex.Column}: {ex.GetCodeLine()}");
                Console.WriteLine();
                return null;
            }
            WalkContext context = new WalkContext();
            // context.Debug = true;
            Dictionary<string, Dictionary<int, Machine>> compiled = ProcessTopLevel(ast.Body, context, path, esdFilter);
            if (compiled == null) return null;
            Dictionary<string, ESD> ret = new Dictionary<string, ESD>();
            foreach (KeyValuePair<string, Dictionary<int, Machine>> entry in compiled)
            {
                if (entry.Value == null)
                {
                    // May happen if filtered out
                    ret[entry.Key] = null;
                }
                else
                {
                    ret[entry.Key] = MakeESD(entry.Key, entry.Value, baseESD);
                }
            }
            return ret;
        }
        public ESD MakeESD(string mEsd, Dictionary<int, Machine> machines, ESD o)
        {
            ESD esd = new ESD(o.LongFormat, o.DarkSoulsCount);
            esd.Unk70 = o.Unk70;
            esd.Unk74 = o.Unk74;
            esd.Unk78 = o.Unk78;
            esd.Unk7C = o.Unk7C;
            byte[] uncond = EzSembler.AssembleExpression(ezContext, "1");
            // Add all state groups
            foreach (KeyValuePair<int, Machine> machineEntry in machines)
            {
                int machineID = machineEntry.Key;
                Machine machine = machineEntry.Value;
                Dictionary<long, ESD.State> states = new Dictionary<long, ESD.State>();
                foreach (KeyValuePair<int, State> entry in machine.States)
                {
                    int id = entry.Key;
                    State state = entry.Value;
                    // if (mEsd == "t110600" && machineID == 2147483641) Console.WriteLine($"{id}: {state}");
                    ESD.State to = new ESD.State();
                    foreach (Condition cond in state.Conditions)
                    {
                        ESD.Condition toCond = new ESD.Condition();
                        // TODO: subconditions
                        if (cond.TargetState != null)
                        {
                            int target = (int)cond.TargetState;
                            if (!machine.States.ContainsKey(target)) throw new Exception($"Added target to {target} which does not exit in {mEsd} {state}");
                            toCond.TargetState = target;
                        }
                        if (cond.Pass != null) toCond.PassCommands = EzSembler.AssembleCommandScript(ezContext, cond.Pass);
                        toCond.Evaluator = cond.Expr == null ? uncond : EzSembler.AssembleExpression(ezContext, cond.Expr);
                        to.Conditions.Add(toCond);
                    }
                    if (state.Entry != null) to.EntryCommands = EzSembler.AssembleCommandScript(ezContext, state.Entry);
                    if (state.While != null) to.WhileCommands = EzSembler.AssembleCommandScript(ezContext, state.While);
                    if (state.Exit != null) to.ExitCommands = EzSembler.AssembleCommandScript(ezContext, state.Exit);
                    states[id] = to;
                }
                esd.StateGroups[machineID] = states;
            }
            return esd;
        }
        // Lots of values which are scoped either globally or to the current lexical node in compilation
        public class WalkContext
        {
            // Global properties
            public bool Debug { get; set; }
            public List<WalkError> Errors = new List<WalkError>();
            public Dictionary<string, (string, int)> Machines = new Dictionary<string, (string, int)>();
            public Dictionary<string, List<CommandParam>> AllParams = new Dictionary<string, List<CommandParam>>();
            public void Error(Py.Node node, string text=null)
            {
                if (Debug) Console.WriteLine($"ERROR: {text}");
                Errors.Add(new WalkError { Node = node, Text = text, Machine = Machine });
            }
            public void Error(string text)
            {
                Error(null, text);
            }
            public CommandParam Param(string funcName, string argName)
            {
                if (!AllParams.ContainsKey(funcName)) return null;
                return AllParams[funcName].Find(param => param.Name == argName);
            }
            // Per-machine properties
            public string Machine { get; set; }
            public List<int> UsedStates { get; set; }
            public (string, int) ID { get => Machines[Machine]; }
            public int ParamIndex(string argName)
            {
                return AllParams[Machine].FindIndex(param => param.Name == argName);
            }
            // Per-node properties
            public bool InCommand { get; set; }
            public bool InCond { get; set; }
            // Clone
            public WalkContext Copy(string machine=null, bool inCommand=false, bool inCond=false)
            {
                WalkContext other = (WalkContext)MemberwiseClone();
                if (machine != null)
                {
                    other.Machine = machine;
                    other.UsedStates = new List<int>();
                }
                if (inCommand) other.InCommand = true;
                if (inCond) other.InCond = true;
                return other;
            }
        }
        public class WalkError
        {
            public Py.Node Node { get; set; }
            public string Text { get; set; }
            public string Machine { get; set; }
        }
        public Dictionary<string, Dictionary<int, Machine>> ProcessTopLevel(Py.Statement node, WalkContext context, string path, Predicate<string> esdFilter = null)
        {
            bool debug = context.Debug;
            // Find all machines
            List<Py.Statement> nodes = node is Py.SuiteStatement suite ? suite.Statements.ToList() : new List<Py.Statement>();
            for (int i = 0; i < nodes.Count; i++)
            {
                Py.Statement stmt = nodes[i];
                if (stmt is Py.ExpressionStatement expr && expr.Expression is Py.ConstantExpression ce && ce.Value is string)
                {
                    if (i != 0) context.Error(stmt, "Docstring at top level but not first statement in the file");
                }
                else if (stmt is Py.FunctionDefinition func)
                {
                    if (func.IsLambda)
                    {
                        // Probably not possible
                        context.Error(stmt, "Top-level functions must be named");
                        continue;
                    }
                    string[] parts = func.Name.Split('_');
                    if (parts.Length < 2)
                    {
                        context.Error(stmt, $"Unexpected name format {func.Name} - expected \"<esd name>_<machine id>\", potentially with other underscore segments in the middle");
                    }
                    string mEsd = parts.First();
                    string mIdStr = parts.Last();
                    if (!int.TryParse(mIdStr, out int mId))
                    {
                        if (mIdStr.StartsWith("x") && int.TryParse(mIdStr.Substring(1), out int diffpart))
                        {
                            mId = 0x7FFFFFFF - diffpart;
                        }
                        else
                        {
                            context.Error(stmt, $"Could not determine machine id from name {func.Name}");
                            mId = 666;
                        }
                    }
                    List<CommandParam> paramList = new List<CommandParam>();
                    for (int j = 0; j < func.Parameters.Count; j++)
                    {
                        Py.Parameter param = func.Parameters[j];
                        if (param.IsList || param.IsDictionary)
                        {
                            context.Error(param, $"*args or **kwargs are not supported");
                        }
                        CommandParam mparam = new CommandParam { Name = param.Name, Index = j };
                        if (debug) Console.WriteLine($"Param {param.Name}, List {param.IsList} Dict {param.IsDictionary} Default {param.DefaultValue}");
                        if (param.DefaultValue is Py.NameExpression name && name.Name == "_")
                        {
                            // No default - for when there are non-default args after a default arg
                        }
                        else if (param.DefaultValue != null)
                        {
                            if (hasConstant(param.DefaultValue, out object val))
                            {
                                mparam.Default = val;
                            }
                            else
                            {
                                context.Error(param.DefaultValue, $"Unrecognized default value {param.DefaultValue} - use _ to mean no default or use a constant expression otherwise");
                            }
                        }
                        paramList.Add(mparam);
                    }
                    context.Machines[func.Name] = (mEsd, mId);
                    context.AllParams[func.Name] = paramList;
                }
            }
            Dictionary<string, Dictionary<int, Machine>> compiled = new Dictionary<string, Dictionary<int, Machine>>();
            foreach (Py.Statement stmt in nodes)
            {
                if (stmt is Py.FunctionDefinition func && !func.IsLambda)
                {
                    if (debug) Console.WriteLine($"def {func.Name}");
                    WalkContext machineContext = context.Copy(machine: func.Name);
                    (string mEsd, int mId) = machineContext.ID;
                    // Don't fully compile if filtered out
                    if (esdFilter != null && !esdFilter(mEsd))
                    {
                        compiled[mEsd] = null;
                        continue;
                    }

                    ProgramNode machine = WalkStatement(func.Body, machineContext, 1);
                    // Next need to rewrite all of trees to assign state breaks
                    // Can DebugProgramNode if necessary. cond like (mEsd == "t110600" && mId == 2147483641)
                    Machine result = AddStateBreaks(machine, machineContext);
                    if (!compiled.ContainsKey(mEsd)) compiled[mEsd] = new Dictionary<int, Machine>();
                    if (compiled[mEsd].ContainsKey(mId))
                    {
                        // These *should* be identical. A bit weird though.
                        // machineContext.Error("Machine already exists");
                        // PrintProgramNode(machine, 1, new Dictionary<string, string>());
                    }
                    else
                    {
                        compiled[mEsd][mId] = result;
                    }
                }
            }
            if (context.Errors.Count == 0)
            {
                return compiled;
            }
            else
            {
                List<(int, string)> lines = new List<(int, string)>();
                TrackingReader reader = new TrackingReader { Reader = File.OpenText(path) };
                while (true)
                {
                    int position = reader.Position;
                    string line = reader.ReadLine();
                    if (line == null)
                    {
                        break;
                    }
                    lines.Add((position, line));
                }
                HashSet<string> printedMachines = new HashSet<string>();
                // TODO: Sort this list perhaps by file position
                foreach (WalkError err in context.Errors)
                {
                    // Print of partially constructed machine for debug
                    if (err.Node == null && err.Machine != null && !printedMachines.Contains(err.Machine))
                    {
                        (string mEsd, int mId) = context.Machines[err.Machine];
                        Console.WriteLine();
                        Console.WriteLine($"def {mEsd}_{FormatMachine(mId)}():  # Reconstructed");
                        PrintProgramNode(compiled[mEsd][mId].Node, 1, new Dictionary<string, string>());
                        Console.WriteLine();
                        printedMachines.Add(err.Machine);
                    }
                    Console.WriteLine($"ERROR{(err.Machine == null ? "" : $" in {err.Machine}")}: {err.Text}");
                    if (err.Node != null && lines.Count > 0)
                    {
                        int start = err.Node.StartIndex;
                        int nextLineIndex = lines.FindIndex(e => e.Item1 > start);
                        int index = Math.Max(0, Math.Min(nextLineIndex - 1, lines.Count - 1));
                        (int pos, string line) = lines[index];
                        Console.WriteLine($"{path}:{index + 1}:{start - pos}: {line}");
                    }
                    Console.WriteLine();
                }
                return null;
            }
        }
        // https://stackoverflow.com/questions/2594125/reading-text-files-line-by-line-with-exact-offset-position-reporting
        class TrackingReader : TextReader
        {
            public TextReader Reader { get; set; }
            public int Position = 0;

            public override int Read()
            {
                this.Position++;
                return Reader.Read();
            }
            public override int Peek()
            {
                return Reader.Peek();
            }
        }
        public Machine AddStateBreaks(ProgramNode machine, WalkContext context)
        {
            // Assign states to all statements (except if statements and jump targets), also adding map for loops/labels on this pass
            Dictionary<string, int> loops = new Dictionary<string, int>();
            Dictionary<string, int> labels = new Dictionary<string, int>();
            SortedDictionary<int, State> states = new SortedDictionary<int, State>();
            HashSet<int> usedStates = new HashSet<int>(context.UsedStates);
            if (usedStates.Count != context.UsedStates.Count)
            {
                context.Error("Duplicate state declarations");
            }
            int machineID = context.ID.Item2;
            State state = null;
            Condition cond = null;
            int nextID = 0;
            ControlMode mode = ControlMode.START;
            void newState(int hint = -1)
            {
                int ID;
                if (hint == -1)
                {
                    while (usedStates.Contains(nextID))
                    {
                        nextID++;
                    }
                    ID = nextID++;
                    // Not an error in general, but it is for state preservation
                    if (!options.Flag("newstates"))
                    {
                        context.Error($"Have to create state {ID}");
                    }
                }
                else
                {
                    ID = hint;
                }
                if (states.ContainsKey(ID))
                {
                    context.Error($"State {ID} used in more than one place");
                }
                else
                {
                    states[ID] = new State
                    {
                        Machine = machineID,
                        ID = ID
                    };
                }
                state = states[ID];
                mode = ControlMode.START;
            }
            void endState()
            {
                state = null;
                mode = ControlMode.START;
            }
            void constructStates(ProgramNode node)
            {
                if (node is ProgSeq seq)
                {
                    foreach (ProgramNode sub in seq.Nodes)
                    {
                        constructStates(sub);
                    }
                    seq.State = seq.Nodes[0].State;
                }
                else if (node is ProgNext next)
                {
                    if (next.Call != null || next.PreBranch != null)
                    {
                        context.Error("Internal error - branching node shouldn't already have a call or prebranch nodes");
                    }
                    if (state == null || mode == ControlMode.POST_CONDITION) newState();
                    // Figure out situation with calls
                    string formatCall(Statement st)
                    {
                        if (!st.Name.StartsWith("6:") || !int.TryParse(st.Name.Substring(2), out int val)) return st.Name;
                        return FormatMachine(val);
                    }
                    List<Statement> condCalls = new List<Statement>();
                    bool usesCalls = false;
                    Expr replaceCalls(Expr expr, Expr parent)
                    {
                        if (expr is FunctionCall call && call.Name.StartsWith("6:"))
                        {
                            Statement callSt = new Statement { Name = call.Name, Args = call.Args };
                            condCalls.Add(callSt);
                            // Probably an explicit comparison... allow this syntax, even if it is not output by decompiler
                            if (parent is BinaryExpr be && ComparisonOps.Contains(be.Op)) return new CallResult();
                            return new BinaryExpr { Op = "!=", Lhs = new CallResult(), Rhs = new CallOngoing() };
                        }
                        else if (expr is CallResult)
                        {
                            usesCalls = true;
                        }
                        return null;
                    }
                    AstVisitor visitor = AstVisitor.Post(replaceCalls);
                    foreach (ProgBranch branch in next.Branches)
                    {
                        if (branch.Cond.Expr != null) branch.Cond.Expr = branch.Cond.Expr.Visit(visitor);
                    }
                    // Make sure the call that applies to this conditional block, if any, is clear
                    if (condCalls.Count > 1)
                    {
                        context.Error($"Can't use multiple calls to other machines ({string.Join(", ", condCalls.Select(st => formatCall(st)))}) in one set of conditions");
                    }
                    if (condCalls.Count > 0 && usesCalls)
                    {
                        context.Error($"Set of conditions contains both machine calls ({string.Join(", ", condCalls.Select(st => formatCall(st)))}) and uses the results of a call - split them out instead");
                    }
                    // Check for preexisting call
                    if (state.Entry != null && state.Entry.Cmds.Last().Name.StartsWith("6:"))
                    {
                        Statement callSt = state.Entry.Cmds.Last();
                        // There is nothing to do to the AST itself, because it is at the end of entry block.
                        if (condCalls.Count > 0)
                        {
                            if (state.While != null)
                            {
                                // context.Error($"Function call {formatCall(callSt)} will cancel instantaneously because of conditional call {formatCall(condCalls[0])}");
                            }
                            // But if there is a call in the conditional itself, a new state is required
                            newState();
                        }
                    }
                    else if (usesCalls)
                    {
                        context.Error($"Call result is used in set of conditions but no call found");
                    }
                    if (condCalls.Count > 0)
                    {
                        if (state.Entry == null) state.Entry = new Block { Cmds = new List<Statement>() };
                        state.Entry.Cmds.Add(condCalls[0]);
                    }
                    // Now calculate states for all conditions
                    node.State = state.ID;
                    State root = state;
                    foreach (ProgBranch branch in next.Branches)
                    {
                        state = root;
                        cond = branch.Cond;
                        state.Conditions.Add(cond);
                        if (branch.Result != null)
                        {
                            mode = ControlMode.POST_CONDITION;
                            constructStates(branch.Result);
                        }
                    }
                    endState();
                }
                else if (node is ProgJump jump)
                {
                    // nothing necessarily to do here?
                    // if (state == null) newState();
                    // jump.State = state.ID;
                    // endState();
                }
                else if (node is ProgLoop loop)
                {
                    // if (state == null || mode != ControlMode.START) newState();
                    // Loop has no state of its own, just the state of the first element
                    constructStates(loop.Node);
                    loop.State = loop.Node.State;
                    if (loop.Label != null) loops[loop.Label] = loop.State;
                    endState();
                }
                else if (node is ProgLabel label)
                {
                    if (state == null || mode != ControlMode.START) newState();
                    label.State = state.ID;
                    labels[label.Label] = state.ID;
                }
                else if (node is ProgReturn ret)
                {
                    if (ret.Value != null)
                    {
                        if (state == null || (mode != ControlMode.START && mode != ControlMode.ENTRY_COMMANDS)) newState();
                    }
                    ret.State = state.ID;
                    if (ret.Value != null)
                    {
                        cond = new Condition();
                        Statement pass = new Statement { Name = "7:-1", Args = new List<Expr> { new ConstExpr { Value = ret.Value } } };
                        cond.Pass = new Block { Cmds = new List<Statement> { pass } };
                        state.Conditions.Add(cond);
                    }
                    endState();
                }
                else if (node is ProgAnnotation ann)
                {
                    foreach (int declared in ann.States)
                    {
                        newState(declared);
                    }
                    ann.State = state.ID;
                }
                else if (node is ProgBlock block)
                {
                    if (block.Operation == null)
                    {
                        List<Statement> stmts = block.Statements;
                        if (state != null && mode == ControlMode.POST_CONDITION)
                        {
                            if (stmts[0].Name == "DebugEvent" || stmts[0].Name == "DebugLogOutput")
                            {
                                if (cond.Pass == null)
                                {
                                    cond.Pass = Block.MakeEmpty();
                                }
                                else
                                {
                                    context.Error("Internal error - condition already had pass block");
                                }
                                cond.Pass.Cmds.Add(stmts[0]);
                                // May be overridden below
                                block.State = state.ID;
                                endState();
                                // Edit statements - to identify pass blocks when constructing jumps
                                stmts.RemoveAt(0);
                                if (stmts.Count == 0) return;
                            }
                        }
                        foreach (Statement st in stmts)
                        {
                            if (state == null || (mode != ControlMode.START && mode != ControlMode.ENTRY_COMMANDS)) newState();
                            block.State = state.ID;
                            // Make entry block if not exists - or reuse existing; ProgBlocks are fine to merge together if there is no call in the middle
                            if (state.Entry == null) state.Entry = Block.MakeEmpty();
                            state.Entry.Cmds.Add(st);
                            // If call, may only appear at the end of an entry block
                            mode = st.Name.StartsWith("6:") ? ControlMode.CALL : ControlMode.ENTRY_COMMANDS;
                        }
                    }
                    else
                    {
                        bool exit = block.Operation == "ExitPause";
                        if (block.Statements.Any(st => st.Name.StartsWith("6:")))
                        {
                            // Maybe do this in AST walker itself?
                            context.Error($"{block.Operation} block contains call");
                        }
                        if (state != null && mode == ControlMode.PAUSE_COMMANDS)
                        {
                            // Can keep state if this type of block has not been processed yet
                            if ((exit ? state.Exit : state.While) != null) newState();
                        }
                        else if (state == null || (mode != ControlMode.START && mode != ControlMode.CALL && mode != ControlMode.ENTRY_COMMANDS)) newState();
                        block.State = state.ID;
                        if (exit)
                        {
                            state.Exit = new Block { Cmds = block.Statements };
                        }
                        else
                        {
                            state.While = new Block { Cmds = block.Statements };
                        }
                    }
                }
            }
            constructStates(machine);
            // Then, add target states for all jumps and conditions
            int nextState = -1;
            HashSet<int> nextHandled = new HashSet<int>();
            void useUnconditionalTransition(int from, Func<string> desc)
            {
                if (from != nextState && nextState != -1)
                {
                    if (!states.ContainsKey(from)) throw new Exception($"Unknown state {from}");
                    State ls = states[from];
                    if (ls.Conditions.Count != 0)
                    {
                        context.Error($"State transition already exists for {desc()} in {from} while trying to add transition to {nextState}");
                    }
                    else
                    {
                        ls.Conditions.Add(new Condition { TargetState = nextState });
                    }
                }
                nextState = from;
            }
            void constructJumps(ProgramNode node, List<(string, int, int)> loopStack)
            {
                int after = nextState;
                if (node is ProgSeq seq)
                {
                    foreach (ProgramNode sub in Enumerable.Reverse(seq.Nodes))
                    {
                        constructJumps(sub, loopStack);
                    }
                }
                else if (node is ProgNext next)
                {
                    foreach (ProgBranch branch in next.Branches)
                    {
                        nextState = after;
                        if (branch.Result == null)
                        {
                            branch.Cond.TargetState = nextState;
                        }
                        else
                        {
                            constructJumps(branch.Result, loopStack);
                            // TODO: Make this work for non-cfgs
                            if (options.Flag("cfg") && nextState == after) context.Error($"Internal error - if/else branch at {nextState} had no associated states");
                            branch.Cond.TargetState = nextState;
                        }
                    }
                    nextState = next.State;
                }
                else if (node is ProgJump jump)
                {
                    // after is ignored
                    if (jump.Type == JumpType.Goto)
                    {
                        nextState = labels[jump.Label];
                    }
                    else
                    {
                        (string, int, int) loop;
                        if (jump.LabelImplied)
                        {
                            if (loopStack.Count == 0)
                            {
                                context.Error($"{jump.Type} from {jump.State} outside of loop");
                                return;
                            }
                            loop = loopStack[loopStack.Count - 1];
                        }
                        else
                        {
                            if (!loops.ContainsKey(jump.Label))
                            {
                                context.Error($"{jump.Type} from {jump.State} to non-existent loop {jump.Label}");
                                return;
                            }
                            loop = loopStack.Where(s => s.Item1 == jump.Label).FirstOrDefault();
                            if (loop.Item1 == null)
                            {
                                context.Error($"{jump.Type} to {jump.Label} from {jump.State} found outside of that loop");
                                return;
                            }
                        }
                        nextState = jump.Type == JumpType.Continue ? loop.Item2 : loop.Item3;
                    }
                }
                else if (node is ProgLoop loop)
                {
                    // after is only used for breaks
                    loopStack = loopStack.ToList();
                    // if (context.Machine == "t110600_x6") Console.WriteLine($">>>>>>> Adding loop {loop.Label} {loop.State} {after}");
                    loopStack.Add((loop.Label, loop.State, after));
                    nextState = loop.State;
                    constructJumps(loop.Node, loopStack);
                    nextState = loop.State;
                    // if (context.Machine == "t110600_x6") Console.WriteLine($">>>>>>> Next state {nextState}");
                }
                else if (node is ProgLabel label)
                {
                    useUnconditionalTransition(label.State, () => $"label {label.Label}");
                }
                else if (node is ProgReturn ret)
                {
                    // after is ignored
                    nextState = ret.State;
                }
                else if (node is ProgAnnotation ann)
                {
                    foreach (int declared in Enumerable.Reverse(ann.States))
                    {
                        useUnconditionalTransition(declared, () => $"declaration of state");
                    }
                }
                else if (node is ProgBlock block)
                {
                    if (block.Statements.Count == 0)
                    {
                        // Pass block - nothing to do here
                        return;
                    }
                    useUnconditionalTransition(block.State, () => $"statement block");
                }
            }
            constructJumps(machine, new List<(string, int, int)>());
            // Finally, 'decompile' conditions into the original ESD format
            // Can avoid doing this for now, DS1 subconditions aren't strictly required...
            return new Machine
            {
                Node = machine,
                ID = machineID,
                States = states,
            };
        }
        enum ControlMode { START, ENTRY_COMMANDS, CALL, PAUSE_COMMANDS, POST_CONDITION }
        // Don't use PythonWalker because we need to transform the entire AST anyway, and explicitly reject unsupported syntax.
        // Docs: http://docs.buddywing.com/html/T_IronPython_Compiler_Ast_Node.htm
        public ProgramNode WalkStatement(Py.Statement node, WalkContext context, int d, bool inIfElse=false)
        {
            // TODO: Import and FromImport?
            bool debug = context.Debug;
            string col = "  ";
            string sp = string.Concat(Enumerable.Repeat(col, d));

            if (node == null)
            {
                if (debug) Console.WriteLine($"{sp}- null");
                context.Error(node, "Internal error - null node");
                return new ProgError();
            }
            if (debug) Console.WriteLine($"{sp}- {node}");
            if (node is Py.SuiteStatement suite)
            {
                // TODO: Use where specifically needed? Or is this top level case fine
                // Used whenever new level of indentation. This happens in function definition, in if statement, and in loop bodies
                List<ProgramNode> nodes = new List<ProgramNode>();
                foreach (Py.Statement stmt in suite.Statements)
                {
                    if (inIfElse && stmt is Py.EmptyStatement)
                    {
                        if (suite.Statements.Count > 1) continue;
                        context.Error(stmt, "internal error - pass statement is the only statement in if/else context, but not detected as empty block");
                    }
                    nodes.Add(WalkStatement(stmt, context, d + 1, inIfElse));
                }
                return ProgSeq.From(nodes);
            }
            else if (node is Py.FunctionDefinition func)
            {
                // This happens at top level (taken care of elsewhere) and in while/exit blocks
                // Name should be non-null (no lambdas). also no generators.
                // TODO: Should also disable calls?
                if (func.IsLambda || func.Parameters.Count > 0 || (func.Name != "ExitPause" && func.Name != "WhilePaused"))
                {
                    context.Error(node, $"Nested function not named ExitPause or WhilePaused, or has parameters - should only be used for while/exit scripts");
                }
                if (debug) Console.WriteLine($"{sp}def {func.Name}");
                ProgramNode body = WalkStatement(func.Body, context, d + 1);
                // body = body is ProgSeq seq ? seq.Simplify() : body;
                List<Statement> statements = new List<Statement>();
                if (body is ProgBlock block)
                {
                    statements = block.Statements;
                }
                else if (body is ProgSeq subseq)
                {
                    foreach (ProgramNode sub in subseq.Nodes)
                    {
                        if (sub is ProgBlock subblock)
                        {
                            statements.AddRange(subblock.Statements);
                        }
                        else
                        {
                            context.Error(node, $"Parts of {func.Name} should be a straight-line sequence of commands only");
                        }
                    }
                }
                return new ProgBlock { Operation = func.Name, Statements = statements };
            }
            else if (node is Py.WhileStatement loop)
            {
                // This happens in loop
                // Don't really need to walk loop - can directly explore
                // TODO: ElseStatement
                if (debug) Console.WriteLine($"{sp}Loop");
                ProgLoop loopNode = new ProgLoop();
                if (loop.Test is Py.NameExpression name && name.Name == "True")
                {
                    // Unnamed loop
                }
                else if (loop.Test is Py.CallExpression call && hasName(call, out string callName) && callName == "Loop" && hasSimpleArg(call, out string arg))
                {
                    loopNode.Label = arg;
                }
                else
                {
                    context.Error(node, "Loop conditions must be unconditional; either True or Loop('looplabel') if labelled");
                }
                loopNode.Node = WalkStatement(loop.Body, context, d + 1);
                return loopNode;
            }
            else if (node is Py.IfStatement ifelse)
            {
                ProgNext next = new ProgNext();
                bool isSimplePass(Py.Statement st)
                {
                    return st is Py.EmptyStatement || (st is Py.SuiteStatement resSuite && resSuite.Statements.Count == 1 && resSuite.Statements[0] is Py.EmptyStatement);
                }
                // This happens for conditional state transitions
                WalkContext condContext = context.Copy(inCond: true);
                foreach (Py.IfStatementTest test in ifelse.Tests)
                {
                    ProgBranch branch = new ProgBranch();
                    next.Branches.Add(branch);
                    if (debug) Console.WriteLine($"{sp}Cond");
                    Expr condExpr = null;
                    if (!(test.Test is Py.NameExpression name && name.Name == "True"))
                    {
                        condExpr = WalkExpr(test.Test, condContext, d + 1);
                    }
                    branch.Cond = new Condition { Expr = condExpr };
                    if (debug) Console.WriteLine($"{sp}Body");
                    if (!isSimplePass(test.Body))
                    {
                        branch.Result = WalkStatement(test.Body, context, d + 1, true);
                    }
                }
                if (ifelse.ElseStatement != null)
                {
                    if (debug) Console.WriteLine($"{sp}Else");
                    ProgBranch branch = new ProgBranch();
                    next.Branches.Add(branch);
                    branch.Cond = new Condition();
                    if (!isSimplePass(ifelse.ElseStatement))
                    {
                        branch.Result = WalkStatement(ifelse.ElseStatement, context, d + 1, true);
                    }
                }
                return next;
            }
            else if (node is Py.AssertStatement assert)
            {
                // This happens for conditional state transitions
                // TODO: Handle Message
                if (assert.Message != null)
                {
                    context.Error(node, $"assert with message is not supported");
                }
                ProgNext next = new ProgNext();
                ProgBranch branch = new ProgBranch();
                next.Branches.Add(branch);
                WalkContext condContext = context.Copy(inCond: true);
                Expr condExpr = WalkExpr(assert.Test, condContext, d + 1);
                branch.Cond = new Condition { Expr = condExpr };
                return next;
            }
            else if (node is Py.ExpressionStatement exprSt)
            {
                // This can be a few things
                // ConstantExpression: doc string, annotates state
                // CallExpression: command, machine call, or special instruction (Goto/Continue/Break/Quit/Label)
                Py.Expression expr = exprSt.Expression;
                if (expr is Py.ConstantExpression ce && ce.Value is string doc)
                {
                    string[] parts = doc.Trim().Split(' ');
                    ProgAnnotation ann = new ProgAnnotation();
                    if (parts.Length >= 2 && parts[0] == "State")
                    {
                        string[] states = parts[1].Split(',');
                        foreach (string stateStr in states)
                        {
                            if (int.TryParse(stateStr, out int stateId))
                            {
                                ann.States.Add(stateId);
                            }
                            else
                            {
                                ann.States.Clear();
                                break;
                            }
                        }
                    }
                    if (ann.States.Count == 0)
                    {
                        context.Error(node, "Unknown doc string format - should start with \"State\" and ids, like \"State 1\" or \"State 3,4\"");
                        return new ProgError();
                    }
                    context.UsedStates.AddRange(ann.States);
                    return ann;
                }
                else if (expr is Py.CallExpression call)
                {
                    if (!(hasName(call, out string name)))
                    {
                        context.Error(node, "Only statically known functions may be called");
                        return new ProgError();
                    }
                    if (name == "Quit")
                    {
                        if (call.Args.Count > 0)
                        {
                            context.Error(node, "Quit does not take any arguments");
                        }
                        return new ProgReturn();
                    }
                    else if (name == "Goto" || name == "Continue" || name == "Break" || name == "Label")
                    {
                        if (!hasSimpleArg(call, out string arg))
                        {
                            context.Error(node, $"Function {name} should take one single string arg for the label");
                        }
                        if (name == "Label")
                        {
                            return new ProgLabel { Label = arg };
                        }
                        JumpType jump = (JumpType)Enum.Parse(typeof(JumpType), name);
                        return new ProgJump { Label = arg, Type = jump };
                    }
                    else
                    {
                        // It's a command
                        Expr e = WalkExpr(expr, context.Copy(inCommand: true), d + 1);
                        if (e is FunctionCall callExpr)
                        {
                            // TODO: Command validation
                            Statement st = new Statement { Name = callExpr.Name, Args = callExpr.Args };
                            return new ProgBlock { Statements = new List<Statement> { st } };
                        }
                        else
                        {
                            context.Error(node, "Internal error - function call not recognized");
                            return new ProgError();
                        }
                    }
                }
                else
                {
                    context.Error(node, "Standalone expression");
                    return new ProgError();
                }
            }
            else if (node is Py.EmptyStatement)
            {
                // This happens to transition to next state in lexical structure
                context.Error(node, "Empty statements may only be used standalone as if/else branches");
                return new ProgError();
            }
            else if (node is Py.ContinueStatement)
            {
                // This happens in transition to loop point
                // TODO: Validate it belongs to loop
                return new ProgJump { Type = JumpType.Continue, LabelImplied = true };
            }
            else if (node is Py.BreakStatement)
            {
                // This happens in transition to loop point
                // TODO: Validate it belongs to loop
                return new ProgJump { Type = JumpType.Break, LabelImplied = true };
            }
            else if (node is Py.ReturnStatement ret)
            {
                // This is used to return specific values. BB+ only
                ProgReturn retNode = new ProgReturn();
                if (ret.Expression is Py.ConstantExpression ce && ce.Value is int val)
                {
                    retNode.Value = val;
                }
                else
                {
                    context.Error(node, "Missing or non-int return value");
                }
                return retNode;
            }
            else if (node is Py.AssignmentStatement assign)
            {
                // Used when examining return values
                if (!(assign.Left.Count == 1 && assign.Left[0] is Py.NameExpression name && name.Name == "call"))
                {
                    context.Error(node, "Assignments may only be used with variables named 'call'");
                }
                if (assign.Right is Py.CallExpression call)
                {
                    Expr e = WalkExpr(assign.Right, context.Copy(inCommand: true), d + 1);
                    if (e is FunctionCall callExpr && callExpr.Name.StartsWith("6:"))
                    {
                        Statement st = new Statement { Name = callExpr.Name, Args = callExpr.Args };
                        return new ProgBlock { Statements = new List<Statement> { st } };
                    }
                    else
                    {
                        context.Error(node, "Assignments may only be used for results of calling other machines");
                        return new ProgError();
                    }
                }
                else
                {
                    context.Error(node, "Assignments may only be used for results of calling other machines");
                    return new ProgError();
                }
            }
            else
            {
                if (debug) Console.WriteLine($"{sp}Unknown {node}");
                context.Error(node);
                return new ProgError();
            }
        }
        private static bool hasName(Py.CallExpression call, out string callName)
        {
            callName = null;
            if (call.Target is Py.NameExpression fname)
            {
                callName = fname.Name;
                return true;
            }
            return false;
        }
        private static bool hasSimpleArg<T>(Py.CallExpression call, out T arg)
        {
            arg = default(T);
            if (call.Args.Count != 1 || call.Args[0].Name != null) return false;
            if (call.Args[0].Expression is Py.ConstantExpression ce && ce.Value is T val)
            {
                arg = val;
                return true;
            }
            return false;
        }
        private static bool hasConstant(Py.Expression expr, out object val)
        {
            val = null;
            if (expr is Py.UnaryExpression unary && unary.Op == PythonOperator.Negate && hasConstant(unary.Expression, out object bval))
            {
                if (bval is int ival) val = -ival;
                else if (bval is float fval) val = -fval;
                else if (bval is double dval) val = -dval;
                if (val != null)
                {
                    return true;
                }
            }
            if (expr is Py.ConstantExpression ce && (ce.Value is int || ce.Value is float || ce.Value is double || ce.Value is string))
            {
                val = ce.Value;
                return true;
            }
            return false;
        }
        public Expr WalkExpr(Py.Expression node, WalkContext context, int d)
        {
            bool debug = context.Debug;
            string col = "  ";
            string sp = string.Concat(Enumerable.Repeat(col, d));

            Expr leftChainExprs(List<Py.Expression> exprs, string op, string dstr)
            {
                Expr baseExpr = null;
                foreach (Py.Expression part in exprs)
                {
                    if (debug && baseExpr != null) Console.WriteLine($"{sp}{dstr}");
                    Expr partExpr = WalkExpr(part, context, d + 1);
                    if (baseExpr == null)
                    {
                        baseExpr = partExpr;
                    }
                    else
                    {
                        baseExpr = new BinaryExpr { Op = op, Lhs = baseExpr, Rhs = partExpr };
                    }
                }
                return baseExpr;
            }
            if (debug) Console.WriteLine($"{sp}> {node}");
            if (node is Py.CallExpression call)
            {
                if (call.Target is Py.MemberExpression mem && mem.Target is Py.NameExpression mname && mname.Name == "call")
                {
                    if (mem.Name == "Done" && call.Args.Count == 0)
                    {
                        return new BinaryExpr { Op = "!=", Lhs = new CallResult(), Rhs = new CallOngoing() };
                    }
                    else if (mem.Name == "Get" && call.Args.Count == 0)
                    {
                        return new CallResult();
                    }
                    else
                    {
                        context.Error(node, $"Only methods Done() and Get() may be used on call objects - found {mem.Name}");
                        return new Unknown();
                    }
                }
                if (!(hasName(call, out string name)))
                {
                    context.Error(node, $"Only statically known functions may be called - found {call.Target}");
                    return new Unknown();
                }
                if (debug) Console.WriteLine($"{sp}Name {name}");
                // TODO: Validate name. This is at least done later when writing out the ESD.
                SortedDictionary<int, Expr> indexArgs = new SortedDictionary<int, Expr>();
                foreach (Py.Arg arg in call.Args)
                {
                    if (debug) Console.WriteLine($"{sp}Arg {arg.Name}");
                    // Note: arg names * and ** are used to mean unpacked args
                    // Named args can also only come after unnamed args
                    Expr expr = WalkExpr(arg.Expression, context, d + 1);
                    if (arg.Name == null)
                    {
                        indexArgs[indexArgs.Count] = expr;
                    }
                    else if (context.AllParams.ContainsKey(name))
                    {
                        CommandParam param = context.Param(name, arg.Name);
                        if (param == null)
                        {
                            context.Error(arg, $"Unrecognized function arg {arg.Name} calling {name}");
                        }
                        else
                        {
                            indexArgs[param.Index] = expr;
                        }
                    }
                    else
                    {
                        context.Error(arg, $"Function {name} does not support named arguments");
                        indexArgs[indexArgs.Count] = expr;
                    }
                }
                List<Expr> args = new List<Expr>();
                if (context.AllParams.ContainsKey(name))
                {
                    foreach (CommandParam param in context.AllParams[name])
                    {
                        if (indexArgs.ContainsKey(param.Index))
                        {
                            args.Add(indexArgs[param.Index]);
                        }
                        else
                        {
                            if (param.Default == null)
                            {
                                context.Error(node, $"Argument {param.Name} not given and there is no default value");
                                args.Add(new Unknown());
                            }
                            else
                            {
                                args.Add(new ConstExpr { Value = param.Default });
                            }
                        }
                    }
                }
                else
                {
                    args = indexArgs.Values.ToList();
                }
                // Renaming
                if (context.Machines.ContainsKey(name))
                {
                    (string esdId, int machine) = context.Machines[name];
                    (string myEsd, int myMachine) = context.ID;
                    if (esdId != myEsd)
                    {
                        context.Error(node, $"Calls across ESDs ({myEsd} -> {esdId}) are not possible");
                    }
                    else if (machine == myMachine)
                    {
                        // TODO: Validate recursive calls?
                        context.Error(node, $"Self calls and recursive calls are not possible");
                    }
                    if (!context.InCommand && !context.InCond)
                    {
                        context.Error(node, $"Can only call {name} in condition or in standalone call statement");
                    }
                    name = $"6:{machine}";
                }
                else if (name.StartsWith("c") && context.InCommand && name.Length >= 3)
                {
                    name = $"{name[1]}:{name.Substring(2)}";
                }
                return new FunctionCall { Name = name, Args = args };
            }
            else if (node is Py.NameExpression name)
            {
                // Used for True, function names, and calls - but these are covered by other nodes
                if (debug) Console.WriteLine($"{sp}{name.Name}");
                int index = context.ParamIndex(name.Name);
                if (index >= 0)
                {
                    return new FunctionCall { Name = "StateGroupArg", Args = new List<Expr> { new ConstExpr { Value = index } } };
                }
                context.Error(node, $"Unknown variable {name.Name}");
                return new Unknown();
            }
            else if (node is Py.ConstantExpression con)
            {
                // TODO: What are valid types? Check Type property
                // String, Int32, Double
                if (debug) Console.WriteLine($"{sp}{con.Value.GetType()}: {con.Value}");
                if (hasConstant(con, out object val))
                {
                    return new ConstExpr { Value = val };
                }
                else
                {
                    context.Error(node, $"Unknown constant type {val.GetType()}");
                    return new Unknown();
                }
            }
            else if (node is Py.UnaryExpression unary)
            {
                if (debug) Console.WriteLine($"{sp}UnOp {unary.Op}");
                Expr arg = WalkExpr(unary.Expression, context, d + 1);
                switch (unary.Op)
                {
                    case PythonOperator.Not:
                        return new BinaryExpr { Op = "==", Lhs = arg, Rhs = new ConstExpr { Value = 0 } };
                    case PythonOperator.Negate:
                        // Simplify this to constant if possible, in cases where things should be constants (e.g. machine args)
                        if (hasConstant(unary, out object val)) return new ConstExpr { Value = val };
                        return new UnaryExpr { Op = "N", Arg = arg };
                    default:
                        context.Error(node, $"Unsupported operator {unary.Op}");
                        return new Unknown();
                }
            }
            else if (node is Py.BinaryExpression bin)
            {
                Expr lhs = WalkExpr(bin.Left, context, d + 1);
                if (debug) Console.WriteLine($"{sp}BinOp {bin.Operator}");
                Expr rhs = WalkExpr(bin.Right, context, d + 1);
                string op;
                // "or", "and", "not", "< <= > >= != ==", "+ -", "* /", "N"
                switch (bin.Operator)
                {
                    case PythonOperator.LessThan: op = "<"; break;
                    case PythonOperator.LessThanOrEqual: op = "<="; break;
                    case PythonOperator.GreaterThan: op = ">"; break;
                    case PythonOperator.GreaterThanOrEqual: op = ">="; break;
                    case PythonOperator.NotEqual: op = "!="; break;
                    case PythonOperator.Equal: op = "=="; break;
                    case PythonOperator.Add: op = "+"; break;
                    case PythonOperator.Subtract: op = "-"; break;
                    case PythonOperator.Multiply: op = "*"; break;
                    case PythonOperator.Divide: op = "/"; break;
                    default:
                        context.Error(node, $"Unsupported operator {bin.Operator}");
                        return new Unknown();
                }
                return new BinaryExpr { Op = op, Lhs = lhs, Rhs = rhs };
            }
            else if (node is Py.AndExpression and)
            {
                // The associativity of the IronPython parser is wrong >:(
                // Suppose we start with ((a && b) && c) && d - which we print as a && b && c && d, because these ops are *supposed* to be left associative
                // The AST has this as a && (b && (c && d)). WTF
                // Note that this doesn't apply when there are explicit parens, because there is a ParenExpression.
                List<Py.Expression> exprs = new List<Py.Expression> { and.Left };
                Py.Expression toAdd = and.Right;
                while (toAdd is Py.AndExpression toRewrite)
                {
                    exprs.Add(toRewrite.Left);
                    toAdd = toRewrite.Right;
                }
                exprs.Add(toAdd);
                return leftChainExprs(exprs, "&&", "Op 'and'");
            }
            else if (node is Py.OrExpression or)
            {
                List<Py.Expression> exprs = new List<Py.Expression> { or.Left };
                Py.Expression toAdd = or.Right;
                while (toAdd is Py.OrExpression toRewrite)
                {
                    exprs.Add(toRewrite.Left);
                    toAdd = toRewrite.Right;
                }
                exprs.Add(toAdd);
                return leftChainExprs(exprs, "||", "Op 'or'");
            }
            else if (node is Py.ParenthesisExpression paren)
            {
                return WalkExpr(paren.Expression, context, d);
            }
            else if (node is Py.IndexExpression index)
            {
                if (debug) Console.WriteLine($"{sp}Index {index.Index} or {index.Target}");
                if (index.Target is Py.NameExpression iname && iname.Name == "args" && index.Index is Py.ConstantExpression ic && ic.Value is int ival)
                {
                    // This happens without any real validation. May cause issues potentially?
                    return new FunctionCall { Name = "StateGroupArg", Args = new List<Expr> { new ConstExpr { Value = ival } } };
                }
                else
                {
                    context.Error(node);
                    return new Unknown();
                }
            }
            else if (node is Py.MemberExpression mem)
            {
                // Could be useful for something at some point?
                if (debug) Console.WriteLine($"{sp}Member {mem.Name} of {mem.Target}");
                context.Error(node);
                return new Unknown();
            }
            else
            {
                if (debug) Console.WriteLine($"{sp}Unknown {node}");
                context.Error(node);
                return new Unknown();
            }
        }
    }
}
