﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ESDLang.Doc;
using ESDLang.EzSemble;
using SoulsFormats;
using SoulsIds;

using static ESDLang.EzSemble.AST;
using static SoulsIds.Universe;

namespace ESDLang.Script
{
    public class Common
    {
        // Shared ESD state wrapper used by both compiler and decompiler
        public class State
        {
            public int Machine { get; set; }
            public int ID { get; set; }
            public ESD.State Inner { get; set; }
            public EDD.StateDesc Desc { get; set; }
            public Block Entry { get; set; }
            public Block While { get; set; }
            public Block Exit { get; set; }
            public List<Condition> Conditions = new List<Condition>();
            public List<int> Calls = new List<int>();
            public List<int> Prev = new List<int>();
            public List<int> Next = new List<int>();

            public override string ToString() => $"State({Machine}-{ID}, Entry=[{Entry}], While=[{While}], Exit=[{Exit}], {string.Join(", ", Conditions)})";

            public void VisitConds(AstVisitor visitor, List<Condition> conds=null)
            {
                if (conds == null) conds = Conditions;
                foreach (Condition cond in conds)
                {
                    if (cond.Expr != null)
                    {
                        cond.Expr = cond.Expr.Visit(visitor);
                    }
                    if (cond.Pass != null)
                    {
                        cond.Pass.Visit(visitor);
                    }
                    VisitConds(visitor, cond.Sub);
                }
            }

            public void Visit(AstVisitor visitor)
            {
                if (Entry != null) Entry.Visit(visitor);
                if (While != null) While.Visit(visitor);
                if (Exit != null) Exit.Visit(visitor);
                VisitConds(visitor);
            }

            public List<List<Condition>> FlattenConds() => Conditions.SelectMany(cond => cond.Flatten()).ToList();

            // Optimization to reduce redundant conditions and gotos
            // Needs more investigation across games
            public List<Condition> CombineConds()
            {
                List<Condition> conds = Conditions.SelectMany(cond => cond.Flatten()).Select(cs => Condition.Combine(cs, true)).ToList();
                if (conds.Count <= 1) return conds;
                List<int> eligible = null;
                // Try to have a fast-ish path here
                for (int i = 0; i < conds.Count - 1; i++)
                {
                    if (conds[i].TargetState is int t1 && conds[i + 1].TargetState is int t2 && t1 == t2
                        && conds[i].Expr != null && conds[i].Pass == null
                        && conds[i + 1].Expr != null && conds[i + 1].Pass == null)
                    {
                        if (eligible == null) eligible = Enumerable.Range(-conds.Count, conds.Count).ToList();
                        eligible[i] = t1;
                        eligible[i + 1] = t2;
                    }
                }
                if (eligible == null) return conds;
                // Now the linq spaghetti
                List<List<Condition>> grouping = conds
                    .Select((c, i) => (c, i))
                    .GroupBy(e => eligible[e.Item2])
                    .Select(g => g.Select(e => e.Item1).ToList())
                    .ToList();
                conds = grouping.Select(cs => Condition.Combine(cs, false)).ToList();
                return conds;
            }
        }

        public class Condition
        {
            public ESD.Condition Inner { get; set; }
            public Expr Expr { get; set; }
            public List<Condition> Sub = new List<Condition>();
            public Block Pass { get; set; }
            public int? TargetState { get; set; }
            public int? DupeID { get; set; }

            public override string ToString() => $"Condition({(DupeID is int ? $"DupeID={DupeID}, " : "")}TargetState={TargetState}, Expr={Expr}, Sub=[{string.Join(", ", Sub)}], Pass=[{Pass}])";

            public List<List<Condition>> Flatten()
            {
                List<List<Condition>> ret = new List<List<Condition>>();
                List<Condition> thisCond = new List<Condition> { this };
                if (Sub.Count == 0)
                {
                    ret.Add(thisCond);
                }
                else
                {
                    foreach (Condition sub in Sub)
                    {
                        foreach (List<Condition> subFlat in sub.Flatten())
                        {
                            ret.Add(thisCond.Concat(subFlat).ToList());
                        }
                    }
                }
                return ret;
            }

            // For this condition only, not subconditions
            public int CountCallUsages()
            {
                int counts = 0;
                void countCalls(Expr expr)
                {
                    if (expr is CallResult) counts++;
                }
                if (Expr != null) Expr.Visit(AstVisitor.PostAct(countCalls));
                return counts;
            }

            // Combines expressions for conditions, preserving most properties of the last one in the list
            public static Condition Combine(List<Condition> cond, bool and)
            {
                if (cond.Count == 0) throw new Exception("None in list");
                if (cond.Count == 1) return cond[0];
                Condition baseCond = (Condition)cond.Last().MemberwiseClone();
                // It's up to the caller to ensure null isn't important (especially in 'or' case)
                if (cond.Take(cond.Count - 1).Any(c => c.Pass != null))
                {
                    throw new Exception($"Internal error: losing info in converting {string.Join(", ", cond)}");
                }
                List<Expr> exprs = cond.Where(c => c.Expr != null).Select(c => c.Expr).ToList();
                if (exprs.Count == 0)
                {
                    baseCond.Expr = null;
                }
                else
                {
                    Expr cur = exprs[0];
                    for (int i = 1; i < exprs.Count; i++)
                    {
                        cur = new BinaryExpr { Op = and ? "&&" : "||", Lhs = cur, Rhs = exprs[i] };
                    }
                    baseCond.Expr = cur;
                }
                return baseCond;
            }
        }

        public class ESDStructure
        {
            public SortedDictionary<int, SortedDictionary<int, State>> Machines { get; set; }
            public Dictionary<int, MachineArgs> MachineArgs { get; set; }
            public Dictionary<string, string> GlobalReplace { get; set; }
        }

        public static string FormatMachine(int id)
        {
            string asHex = $"{id:X}";
            if (asHex.StartsWith("7FFF"))
            {
                string suffix = asHex.Substring(4).TrimStart('F');
                id = 0x7FFFFFFF - id;
                // return 'x' + (suffix.Length == 0 ? "F" : suffix);
                return "x" + id;
            }
            return id.ToString();
        }

        public static bool ParseMachine(string mIdStr, out int mId)
        {
            if (!int.TryParse(mIdStr, out mId))
            {
                if (mIdStr.StartsWith("x") && int.TryParse(mIdStr.Substring(1), out int diffpart))
                {
                    mId = 0x7FFFFFFF - diffpart;
                }
                else
                {
                    return false;
                }
            }
            return true;
        }

        public static int MachineSort(int id)
        {
            string asHex = $"{id:X}";
            if (asHex.StartsWith("7FFF"))
            {
                return 0x7FFFFFFF - id + 100000;
            }
            return id;
        }

        // Shared program AST used by both compiler and decompiler
        public class Machine
        {
            public int ID { get; set; }
            public ProgramNode Node { get; set; }
            public ProgramNode Unused { get; set; }
            public SortedDictionary<int, State> States { get; set; }
        }

        public abstract class ProgramNode
        {
            public int State = -1;
            public abstract bool IsEmpty();
            public static bool IsEmpty(ProgramNode node) => node == null || node.IsEmpty();
        }

        public class ProgError : ProgramNode
        {
            public override bool IsEmpty() => true;
        }
        public enum ProgAnnotationType
        {
            // State marker: assign state ids
            States,
            // Pass block marker: use a pass block instead of creating a new state
            Pass,
            // Unused content marker: does nothing
            Unused,
        }
        public class ProgAnnotation : ProgramNode
        {
            public ProgAnnotationType Type { get; set; }
            // Should this be its own node? Or attached to another node?
            // It's a bit hacky now to either show or not show it
            public List<int> States = new List<int>();
            // EDD docs for the states here
            public List<string> StateDoc = new List<string>();
            public override bool IsEmpty() => true;
        }
        public class ProgLabel : ProgramNode
        {
            // Target for gotos
            public string Label { get; set; }
            public override bool IsEmpty() => false;
        }
        public class ProgBlock : ProgramNode
        {
            public string Operation { get; set; }
            public List<Statement> Statements = new List<Statement>();
            public List<string> StmtDocs = new List<string>();
            public void Add(Statement st, string doc = null)
            {
                Statements.Add(st);
                StmtDocs.Add(doc);
            }
            public override bool IsEmpty() => Statements.Count == 0;
        }
        public class ProgNext : ProgramNode
        {
            public Statement Call { get; set; }
            public string CallDoc { get; set; }
            public List<ProgBranch> Branches = new List<ProgBranch>();
            public ProgramNode PreBranch { get; set; }
            public override bool IsEmpty() => Call == null && IsEmpty(PreBranch) && Branches.All(b => b.IsEmpty());
        }
        public class ProgBranch
        {
            public int Target = -1;
            public Condition Cond { get; set; }
            public ProgramNode Result { get; set; }
            public int CallUsages { get; set; }
            public bool IsEmpty() => Cond.Expr == null && ProgramNode.IsEmpty(Result);
        }
        public class ProgJump : ProgramNode
        {
            public JumpType Type { get; set; }
            public int Target { get; set; }
            public bool LabelImplied { get; set; }
            public string Label { get; set; }
            public int LoopIdent { get; set; }
            public override bool IsEmpty() => false;
        }
        public enum JumpType { Goto, Break, Continue };
        public class ProgReturn : ProgramNode
        {
            public int? Value { get; set; }
            public string Doc { get; set; }
            public override bool IsEmpty() => false;
        }
        public class ProgLoop : ProgramNode
        {
            public ProgramNode Node { get; set; }
            public string Label { get; set; }
            public override bool IsEmpty() => false;
        }
        public class ProgSeq : ProgramNode
        {
            public List<ProgramNode> Nodes { get; set; }
            // TODO: Should make it an error to create 0-length sequence?
            public override bool IsEmpty() => Nodes.Count == 0 || Nodes.All(n => IsEmpty(n));
            public static ProgramNode From(List<ProgramNode> nodes, bool simplify = true)
            {
                if (nodes.Count == 0) throw new Exception("No nodes given");
                if (nodes.Count == 1) return nodes[0];
                ProgSeq node = new ProgSeq { State = nodes[0].State, Nodes = nodes };
                return simplify ? From(node.Simplify(), false) : node;
            }
            public List<ProgramNode> Simplify()
            {
                List<ProgramNode> newParts = new List<ProgramNode>();
                foreach (ProgramNode node in Nodes)
                {
                    if (node is ProgSeq subseq)
                    {
                        newParts.AddRange(subseq.Simplify());
                    }
                    else
                    {
                        newParts.Add(node);
                    }
                }
                return newParts;
            }
        }

        // Some utility functions for shared AST
        public static void DebugProgramNode(ProgramNode node, int d)
        {
            string col = "  ";
            string sp = string.Concat(Enumerable.Repeat(col, d));
            string extraInfo = "";
            if (node is ProgBlock block) extraInfo = $" ({block.Statements.Count} statements)";
            Console.WriteLine($"{sp}{(node.State == -1 ? "" : $"{node.State}: ")}{node}{extraInfo}");
            if (node is ProgSeq seq)
            {
                foreach (ProgramNode sub in seq.Nodes)
                {
                    DebugProgramNode(sub, d + 1);
                }
            }
            else if (node is ProgNext next)
            {
                // Extract calls out of conditions, also grouping conditions into subconditions based on call checks
                foreach (ProgBranch branch in next.Branches)
                {
                    Console.WriteLine($"{sp}Cond {branch.Cond.Expr} -> {branch.Cond.TargetState}");
                    if (branch.Result != null)
                    {
                        DebugProgramNode(branch.Result, d + 1);
                    }
                }
            }
            else if (node is ProgLoop loop)
            {
                DebugProgramNode(loop.Node, d + 1);
            }
            if (d == 0) Console.WriteLine();
        }

        public record PrintData(Universe Universe, ESDOptions Options);

        public static void PrintProgramNode(ProgramNode node, int indent, Dictionary<string, string> replace, PrintData data = null)
        {
            string col = "    ";
            string sp = string.Concat(Enumerable.Repeat(col, indent));
            void maybeComment(Statement statement = null, Expr expr = null, string name = null)
            {
                if (name != null)
                {
                    Console.WriteLine($"{sp}# {name}");
                }
                bool combine = false;
                List<string> comments = WriteSourceInfo(data, statement: statement, expr: expr);
                if (comments.Count > 0)
                {
                    if (combine)
                    {
                        comments = new List<string> { string.Join(", ", comments) };
                    }
                    foreach (string str in comments)
                    {
                        string comment = str.Replace("\r", "").Replace("\n", "\\n");
                        Console.WriteLine($"{sp}# {comment}");
                    }
                }
            }
            if (node is ProgAnnotation label)
            {
                if (label.Type == ProgAnnotationType.Pass)
                {
                    Console.WriteLine($"{sp}\"\"\"Pass\"\"\"");
                }
                else if (label.Type == ProgAnnotationType.Unused)
                {
                    Console.WriteLine($"{sp}\"\"\"Unused\"\"\"");
                }
                else if (label.Type == ProgAnnotationType.States)
                {
                    string stateDoc = label.StateDoc.Count == 0 ? null : label.StateDoc.Last();
                    if (stateDoc != null && stateDoc.EndsWith("\"")) stateDoc += " ";
                    Console.WriteLine($"{sp}\"\"\"State {string.Join(",", label.States)}{(stateDoc == null ? "" : $": {stateDoc}")}\"\"\"");
                }
            }
            else if (node is ProgBlock block)
            {
                string sp2 = sp;
                if (block.Operation != null)
                {
                    sp2 += col;
                    Console.WriteLine($"{sp}def {block.Operation}():");
                }
                for (int i = 0; i < block.Statements.Count; i++)
                {
                    Statement st = block.Statements[i];
                    string name = i < block.StmtDocs.Count ? block.StmtDocs[i] : null;
                    maybeComment(statement: st, name: name);
                    Console.WriteLine(WriteStatement(sp2, st, replace));
                }
            }
            else if (node is ProgNext next)
            {
                List<ProgBranch> branches = next.Branches;
                // bool inlineCall = next.Call != null && branches.All(br => br.CallUsages == 1);
                if (branches.Count == 1)
                {
                    ProgBranch branch = branches[0];
                    Dictionary<string, string> subreplace = replace;
                    if (next.Call != null)
                    {
                        if (branch.CallUsages == 1)
                        {
                            // Preblock is an issue here...
                            maybeComment(statement: next.Call, name: next.CallDoc);
                            // TODO: Is this expensive for very large ESDs?
                            subreplace = new Dictionary<string, string>(replace);
                            // This isn't just getting thrown away because next.Call != null means it's a specialCmd which
                            // is the last one in the block, and the CallUsage must be due to branch.Cond.Expr != null.
                            // This system is not great given how complicated the invariants are - can this be transformed before printing?
                            // This can't easily use StringTree, so hopefully most calls are short.
                            subreplace["done"] = subreplace["result"] = WriteStatement(null, next.Call, replace);
                        }
                        else
                        {
                            maybeComment(statement: next.Call, name: next.CallDoc);
                            Console.WriteLine(WriteStatement($"{sp}call = ", next.Call, replace));
                        }
                    }
                    if (next.PreBranch != null)
                    {
                        PrintProgramNode(next.PreBranch, indent, replace, data);
                    }
                    if (branch.Cond.Expr != null)
                    {
                        maybeComment(expr: branch.Cond.Expr);
                        Console.WriteLine(WordWrap($"{sp}assert ", WriteExpr(branch.Cond.Expr, subreplace).Split(' ')));
                    }
                    PrintProgramNode(branch.Result, indent, replace, data);
                }
                else
                {
                    Dictionary<string, string> subreplace = replace;
                    if (next.Call != null)
                    {
                        // TODO: Also use inline call? But that would require syntax to identify when it's being used.
                        // As a result, subreplace is not getting updated.
                        maybeComment(statement: next.Call, name: next.CallDoc);
                        Console.WriteLine(WriteStatement($"{sp}call = ", next.Call, replace));
                    }
                    if (next.PreBranch != null)
                    {
                        PrintProgramNode(next.PreBranch, indent, replace, data);
                    }
                    int num = 0;
                    foreach (ProgBranch branch in branches)
                    {
                        string verb = num == 0 ? "if" : "elif";
                        if (num == branches.Count - 1 && branch.Cond.Expr == null)
                        {
                            Console.WriteLine($"{sp}else:");
                        }
                        else
                        {
                            if (branch.Cond.Expr == null)
                            {
                                Console.WriteLine($"{sp}{verb} True:");
                            }
                            else
                            {
                                maybeComment(expr: branch.Cond.Expr);
                                Console.WriteLine(WordWrap($"{sp}{verb} ", WriteExpr(branch.Cond.Expr, subreplace).Split(' ')) + ":");
                            }
                        }
                        if (branch.Result == null || branch.Result.IsEmpty())
                        {
                            // There can be an annotation here
                            List<ProgAnnotation> progs = new List<ProgAnnotation>();
                            if (branch.Result != null)
                            {
                                if (branch.Result is ProgSeq emptySeq)
                                {
                                    progs.AddRange(emptySeq.Simplify().Select(n => n as ProgAnnotation).Where(n => n != null));
                                }
                                else if (branch.Result is ProgAnnotation ann)
                                {
                                    progs.Add(ann);
                                }
                            }
                            foreach (ProgAnnotation ann in progs)
                            {
                                PrintProgramNode(ann, indent + 1, replace, data);
                            }
                            // This is not strictly needed if there are ProgAnnotations, but it makes output not dependent on printing them or not
                            Console.WriteLine($"{sp}{col}pass");
                        }
                        else
                        {
                            PrintProgramNode(branch.Result, indent + 1, replace, data);
                        }
                        num++;
                    }
                }
            }
            else if (node is ProgJump jump)
            {
                if (jump.LabelImplied)
                {
                    Console.WriteLine($"{sp}{jump.Type.ToString().ToLower()}");
                }
                else
                {
                    Console.WriteLine($"{sp}{jump.Type}('{jump.Label}')");
                }
            }
            else if (node is ProgReturn ret)
            {
                if (ret.Value == null)
                {
                    Console.WriteLine($"{sp}Quit()");
                }
                else
                {
                    Console.WriteLine($"{sp}return {ret.Value}");
                }
            }
            else if (node is ProgLabel labels)
            {
                Console.WriteLine($"{sp}Label('{labels.Label}')");
            }
            else if (node is ProgLoop loop)
            {
                if (loop.Label == null)
                {
                    Console.WriteLine($"{sp}while True:");
                }
                else
                {
                    Console.WriteLine($"{sp}while Loop('{loop.Label}'):");
                }
                PrintProgramNode(loop.Node, indent + 1, replace, data);
            }
            else if (node is ProgSeq seq)
            {
                // Just hacky here - combine labels - can also do this as preprocess step...
                List<ProgramNode> nodes = seq.Simplify();
                for (int i = nodes.Count - 2; i >= 0; i--)
                {
                    if (nodes[i] is ProgAnnotation l1 && nodes[i + 1] is ProgAnnotation l2
                        && l1.Type == ProgAnnotationType.States && l2.Type == ProgAnnotationType.States)
                    {
                        l1.States.AddRange(l2.States);
                        l1.StateDoc.AddRange(l2.StateDoc);
                        nodes.RemoveAt(i + 1);
                    }
                }
                foreach (ProgramNode sub in nodes)
                {
                    PrintProgramNode(sub, indent, replace, data);
                }
            }
        }

        // Arg classes, used to mark machine args and annotate Python programs
        public class ValueUsage
        {
            public List<int> Args = new List<int>();
            public List<Expr> Exprs = new List<Expr>();
            // What an arg means, if a game id
            public IdExtractor Extractor { get; set; }
            // If checked for equality with a constant
            public bool Check { get; set; }
        }

        public class IdExtractor
        {
            public List<int> Indices { get; set; }
            public Func<List<int>, Obj> Extract { get; set; }
            public Namespace Type { get; set; }
        }

        public class ValueSource
        {
            public ConstExpr Value { get; set; }
            public Expr Source { get; set; }
            // public List<ValueUsage> Usages = new List<ValueUsage>();
            public Dictionary<ValueUsage, List<Obj>> Usages = new Dictionary<ValueUsage, List<Obj>>();
        }

        public class MachineArgs
        {
            public int ID { get; set; }
            public int Count = -1;
            public Dictionary<int, List<Statement>> Callers = new Dictionary<int, List<Statement>>();
            // Different usages of args. The args themselves are in the sub-object
            public List<ValueUsage> Usages = new List<ValueUsage>();
            // The call site origins of different values, for different indices
            public List<List<ValueSource>> Values = new List<List<ValueSource>>();
            // The final inferred list of params
            public List<CommandParam> Params = new List<CommandParam>();
        }

        public class CommandParam
        {
            public string Name { get; set; }
            public int Index { get; set; }
            public object Default { get; set; }
            public bool HideInCall { get; set; }
        }

        public static List<string> WriteSourceInfo(PrintData data, Statement statement = null, Expr expr = null)
        {
            Universe u = data?.Universe;
            if (u == null) return new List<string>();
            bool multiline = data.Options?.Flag("dialogue") ?? true;
            List<ValueSource> sources = new List<ValueSource>();
            void addSource(Expr e)
            {
                if (e.SourceInfo != null)
                {
                    sources.Add((ValueSource)e.SourceInfo);
                }
            }
            if (statement != null) statement.Visit(AstVisitor.PreAct(addSource));
            if (expr != null) expr.Visit(AstVisitor.PreAct(addSource));
            List<string> infos = new List<string>();
            HashSet<Obj> objs = new HashSet<Obj>();
            foreach (ValueSource source in sources)
            {
                foreach (KeyValuePair<ValueUsage, List<Obj>> usage in source.Usages)
                {
                    foreach (Obj obj in usage.Value)
                    {
                        if (objs.Contains(obj) || !u.Names.ContainsKey(obj)) continue;
                        objs.Add(obj);
                        if (obj.Type == Namespace.Talk)
                        {
                            int talkId = int.Parse(obj.ID);
                            int i = 0;
                            while (true)
                            {
                                Obj text = Obj.Talk(talkId + i);
                                // TODO: Can universe be null here?
                                if (!u.Names.ContainsKey(text)) break;
                                infos.Add($"{u.Name(text)}");
                                if (!multiline) break;
                                i++;
                            }
                            continue;
                        }
                        infos.Add($"{(u == null ? obj.ToString() : u.Name(obj))}");
                    }
                }
            }
            return infos;
        }

        private readonly static int LineWidth = 110;
        private readonly static string SingleIndent = "    ";

        // For pretty printing recursive structures, based on DarkScript3
        // TODO finish implementing
        /*
         * Because things can get super heavily indented, there's still a line-local limit.
         * Patterns:
         * if (x and y
         *     and z and v):
         * if (x
         *     and y
         *     and z):
         * funcline(
         *     a=1, b=2,
         *     c=3, d=4)
         * funcline(
         *     a=1,
         *     b=2,
         *     c=3)
         * (b1
         *  and not (c1
         *           and d2))
         */
        public class StringTree
        {
            public string Start = "";
            public List<StringTree> Children { get; set; }
            public string Sep = "";
            public string End = "";
            private int _Length;

            private int Length
            {
                get
                {
                    if (_Length == 0)
                    {
                        _Length = (Children != null ? Children.Sum(c => c.Length) + Sep.Length * (Children.Count - 1) : 0) + Start.Length + End.Length;
                    }
                    return _Length;
                }
            }

            // A simple unbreakable string
            public static StringTree Of(object s) => new StringTree { Start = s.ToString() };
            // A start which can appear on its own line when the rest of it is too long
            public static StringTree IsolatedStart(string start, StringTree mid, string end) => new StringTree
            {
                Children = new List<StringTree> { Of(start), mid },
                End = end
            };
            // A start where the rest of it can be broken up, but it doesn't appear on its own line.
            public static StringTree CombinedStart(string start, StringTree mid, string end) => new StringTree
            {
                Start = start,
                Children = new List<StringTree> { mid },
                End = end
            };

            private string RenderOneLine() => Start + (Children == null ? "" : string.Join(Sep, Children.Select(c => c.RenderOneLine()))) + End;

            public string Render(string sp)
            {
                // TODO: Consider passing in a StringBuilder to use recursively for a rather minor efficiency gain.
                // Most printed lines won't use StringTree in any case.
                if (Children == null || Children.Count == 0 || sp.Length + Length <= LineWidth)
                {
                    return RenderOneLine();
                }
                string sp2 = sp + SingleIndent;
                if (Children.Count == 1)
                {
                    return Start + Children[0].Render(sp) + End;
                }
                StringBuilder ret = new StringBuilder();
                ret.AppendLine(Start + Children[0].Render(sp));
                for (int i = 1; i < Children.Count - 1; i++)
                {
                    ret.AppendLine(sp2 + Sep.TrimStart() + Children[i].Render(sp2));
                }
                ret.Append(sp2 + Sep.TrimStart() + Children[Children.Count - 1].Render(sp2) + End);
                return ret.ToString();
            }
        }

        // Utilities to output Python
        // TODO: Rectangle rule please
        public static string WordWrap(string prefix, string[] words, bool alwaysParens = false)
        {
            string text;
            if (prefix.Length + words.Select(w => w.Length).Sum() < LineWidth)
            {
                text = string.Join(" ", words);
            }
            else
            {
                StringBuilder sb = new StringBuilder();
                string spPrefix = string.Concat(Enumerable.Repeat(' ', prefix.Length + 1));
                int localLimit = Math.Max(LineWidth - spPrefix.Length, 40);
                int cur = 0;
                bool first = true;
                foreach (string word in words)
                {
                    if (cur > localLimit)
                    {
                        sb.Append($"\r\n{spPrefix}");
                        cur = 0;
                    }
                    else if (!first)
                    {
                        sb.Append(' ');
                    }
                    first = false;
                    sb.Append(word);
                    cur += word.Length + 1;
                }
                text = sb.ToString();
            }
            return prefix + (alwaysParens || text.Contains("\n") ? $"({text})" : text);
        }

        public static string WriteStatement(string prefix, Statement st, Dictionary<string, string> replace = null)
        {
            string name = st.Name;
            List<string> args = st.Args.Select(e => WriteExpr(e, replace: replace)).ToList();
            if (name == "7:-1") return $"return {args.FirstOrDefault()}";
            if (name.Contains(':'))
            {
                string[] parts = name.Split(':');
                name = $"c{parts[0]}_{parts[1]}";
                args = args.Select((arg, i) => replace.TryGetValue($"{name}_{i}", out string argName) ? $"{argName}={arg}" : arg).ToList();
                if (replace != null && replace.ContainsKey(name)) name = replace[name];
            }
            // Maybe add comma separation as a feature to word warp...
            args = args.Select((arg, i) => arg + (i == st.Args.Count - 1 ? "" : ",")).ToList();
            return prefix == null ? $"{name}({string.Join(" ", args)})" : WordWrap(prefix + name, args.ToArray(), alwaysParens: true);
        }

        public static bool HasBoolOp(Expr expr)
        {
            return expr is BinaryExpr be2 && BoolOps.Contains(be2.Op)
                || expr is UnaryExpr ue2 && BoolOps.Contains(ue2.Op)
                ;//|| expr is FunctionCall fn && fn.Method != null && fn.Method.BinaryReturn;
        }

        public static string WriteExpr(Expr expr, Dictionary<string, string> replace = null, string parent = null, bool rhs = false)
        {
            string s;
            if (expr is ConstExpr ce)
            {
                if (ce.Value is string cs)
                {
                    s = cs.Contains('\'') ? $"\"{cs}\"" : $"'{cs}'";
                }
                else
                {
                    s = ce.Value.ToString();
                    // Special formatting. This is purely an output-time thing for the time being.
                    if (EzSembleContext.UseNew && expr.ArgDoc != null && ce.TryAsInt(out int enumVal))
                    {
                        if (expr.ArgDoc.Enum != null && expr.ArgDoc.Enum.Names.TryGetValue(enumVal, out string enumName))
                        {
                            // Is this always the formatting to use? Flags may want to use ON/OFF
                            s = $"{expr.ArgDoc.Enum.Name}.{enumName}";
                        }
                        else if (expr.ArgDoc.Type == "bool" && (enumVal == 0 || enumVal == 1))
                        {
                            s = enumVal == 1 ? "True" : "False";
                        }
                    }
                }
            }
            else if (expr is UnaryExpr ue)
            {
                // Unary case: (not 1) == 1
                string op = getPythonOp(ue.Op);
                s = $"{op}{(op == "not" ? " " : "")}{WriteExpr(ue.Arg, parent: op, replace: replace)}";
                if (parent == null) return s;
                int prec1 = pythonOpPrec[parent];
                int prec2 = pythonOpPrec[op];
                if (prec1 > prec2)
                {
                    s = $"({s})";
                }
            }
            else if (expr is BinaryExpr be)
            {
                string op = getPythonOp(be.Op);
                // Do some adhoc simplification here
                // One boolean simplification. Should probably transform the Expr to make more
                if (be.Lhs is CallResult)
                {
                    if (op == "!=" && be.Rhs is CallOngoing)
                    {
                        return replace != null && replace.ContainsKey("done") ? replace["done"] : "call.Done()";
                    }
                    string lhs = replace != null && replace.ContainsKey("result") ? replace["result"] : "call.Get()";
                    s = $"{lhs} {op} {WriteExpr(be.Rhs, parent: op, rhs: true, replace: replace)}";
                }
                else
                {
                    s = $"{WriteExpr(be.Lhs, parent: op, replace: replace)} {op} {WriteExpr(be.Rhs, parent: op, rhs: true, replace: replace)}";
                }
                if (parent == null) return s;
                int prec1 = pythonOpPrec[parent];
                int prec2 = pythonOpPrec[op];
                // Add parens to subexpression if operator has lower precedence, i.e. less binding
                // Also add if expression is explicitly written with right associativity
                // Cases: 3/7 + 2, (3+7) / 2, 3 / (7+2), 3 + 7/2, 3+3 + 3, 3 + (3+3)
                // Special exception for and/or because that parens are more readable there.
                // == is also a problem because of chained comparisons in Python (TODO: check this)
                if (prec1 > prec2 || (prec1 == prec2 && rhs) || (op == "and" && parent == "or") || (ComparisonOps.Contains(op) && ComparisonOps.Contains(parent)))
                {
                    s = $"({s})";
                }
            }
            else if (expr is FunctionCall func)
            {
                IEnumerable<string> args = func.Args.Select(e => WriteExpr(e, replace: replace));
                if (func.Name == "StateGroupArg")
                {
                    string index = args.FirstOrDefault();
                    if (replace.TryGetValue($"arg{index}", out string argName))
                    {
                        s = argName;
                    }
                    else
                    {
                        s = $"args[{index}]";
                    }
                }
                else
                {
                    string name = func.Name;
                    s = $"{func.Name}({string.Join(", ", args)})";
                }
            }
            else if (expr is Unknown huh)
            {
                s = $"#{huh.Opcode:X2}";
            }
            else throw new Exception($"Unknown expression subclass {expr.GetType()} in current context");
            return s;
        }

        public static bool TryEvalInt(Expr expr, out int ret, Dictionary<int, int> args=null)
        {
            ret = 0;
            if (expr is ConstExpr ce)
            {
                if (ce.TryAsInt(out int val))
                {
                    ret = val;
                    return true;
                }
            }
            else if (expr is UnaryExpr ue)
            {
                if (ue.Op == "N" && TryEvalInt(ue.Arg, out int val, args))
                {
                    ret = -val;
                    return true;
                }
            }
            else if (expr is BinaryExpr be)
            {
                if (TryEvalInt(be.Lhs, out int a, args) && TryEvalInt(be.Rhs, out int b, args))
                {
                    bool found = true;
                    switch (be.Op)
                    {
                        case "&&": ret = a & b; break;
                        case "||": ret = a | b; break;
                        case "==": ret = a == b ? 1 : 0; break;
                        case "!=": ret = a != b ? 1 : 0; break;
                        case "+": ret = a + b; break;
                        case "-": ret = a - b; break;
                        case "*": ret = a * b; break;
                        case "/": ret = a / b; break;
                        default: found = false; break;
                    }
                    return found;
                }
            }
            else if (expr is FunctionCall func)
            {
                if (func.Name == "StateGroupArg" && args != null)
                {
                    int arg = func.Args[0].AsInt();
                    if (args.ContainsKey(arg))
                    {
                        ret = args[arg];
                        return true;
                    }
                }
            }
            return false;
        }

        public static HashSet<string> ComparisonOps = new HashSet<string> { "<", "<=", ">", ">=", "!=", "==" };

        private static HashSet<string> BoolOps = new HashSet<string> { "!", "&&", "||", "<", "<=", ">", ">=", "!=", "==" };
        private static List<string> pythonOpPrecs = new List<string> { "or", "and", "not", "< <= > >= != ==", "+ -", "* /", "N" };
        private static Dictionary<string, int> pythonOpPrec = pythonOpPrecs.SelectMany((ops, i) => ops.Split(' ').Select(op => (op, i))).ToDictionary(i => i.Item1, i => i.Item2);
        private static Dictionary<string, string> astToPythonOps = new Dictionary<string, string>
        {
            ["&&"] = "and",
            ["||"] = "or",
            ["N"] = "-",
            ["!"] = "not",
        };

        private static string getPythonOp(string op) => astToPythonOps.TryGetValue(op, out string pyOp) ? pyOp : op;
    }
}
