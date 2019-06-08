using System;
using System.Collections.Generic;
using System.Linq;

namespace ESDLang.EzSemble
{
    public class AST
    {
        public class Block
        {
            public List<Statement> Cmds;
            public override string ToString() => string.Join("\n", Cmds.Select(c => $"{c};"));
            public bool Empty => Cmds.Count == 0;

            public Block Copy()
            {
                List<Statement> newCmds = new List<Statement>();
                foreach (Statement st in Cmds)
                {
                    newCmds.Add(st.Copy());
                }
                return new Block { Cmds = newCmds };
            }
            public void Visit(Func<Expr, Expr> previsit = null, Func<Expr, Expr> postvisit = null)
            {
                foreach (Statement st in Cmds)
                {
                    st.Visit(previsit, postvisit);
                }
            }
        }

        public class Statement
        {
            public string Name { get; set; }
            public List<Expr> Args { get; set; }
            public override string ToString() => $"{Name}({string.Join(", ", Args)})";

            public Statement Copy()
            {
                Statement st = (Statement)MemberwiseClone();
                st.Args = st.Args.ToList();
                for (int i = 0; i < st.Args.Count; i++)
                {
                    st.Args[i] = st.Args[i].Copy();
                }
                return st;
            }
            public void Visit(Func<Expr, Expr> previsit = null, Func<Expr, Expr> postvisit = null)
            {
                for (int i = 0; i < Args.Count; i++)
                {
                    Expr newArg = Args[i].Visit(previsit, postvisit);
                    if (newArg != null) Args[i] = newArg;
                }
            }
        }

        public enum FalseCond
        {
            NONE, CONTINUE, ABORT
        }
        public abstract class Expr
        {
            // Any special handling if the expression is false. Seems to be no-op for game ESDs in DS3 and on, used for optimization.
            public FalseCond IfFalse { get; set; }
            // Can preserve AST info after tree rewriting. Possibly dubious feature
            public object SourceInfo { get; set; }

            public int AsInt()
            {
                if (TryAsInt(out int i)) return i;
                throw new Exception($"{this} cannot be used as an int");
            }
            public virtual bool TryAsInt(out int i)
            {
                i = 0;
                return false;
            }

            // These recursive functions are done at top level only for readability, as this AST is not meant to be extensible.
            // Plus it can be used as a model for other serializations.
            public sealed override string ToString() => ToZeditorString(null);
            public string ToZeditorString(string parent=null, bool nonCommute=false)
            {
                Expr expr = this;
                string s;
                if (SourceInfo != null)
                {
                    s = parent == null ? SourceInfo.ToString() : $"{SourceInfo}";
                }
                else if (expr is ConstExpr ce)
                {
                    if (ce.Value is float f) s = f.ToString("R");
                    else if (ce.Value is double d) s = d.ToString("R");
                    else if (ce.Value is string s2) s = $"\"{s2}\"";
                    else s = $"{ce.Value}";
                }
                else if (expr is UnaryExpr ue)
                {
                    s = $"{ue.Op}{ue.Arg.ToZeditorString($"u{ue.Op}")}";
                }
                else if (expr is BinaryExpr be)
                {
                    // Do some adhoc simplification here
                    string op = be.Op;
                    s = $"{be.Lhs.ToZeditorString(op)} {op} {be.Rhs.ToZeditorString(op, true)}";
                    if (parent != null)
                    {
                        if (eqs.Contains(op) && (parent == "&&" || parent == "||"))
                        {
                            // No paren required
                        }
                        else if (nonCommute || !commutes.ContainsKey(op) || !commutes.ContainsKey(parent) || commutes[op] != commutes[parent])
                        {
                            s = $"({s})";
                        }
                    }
                }
                else if (expr is FunctionCall func)
                {
                    s = func.Name == "StateGroupArg" ? $"{func.Name}[{func.Args[0]}]" : $"{func.Name}({string.Join(", ", func.Args)})";
                }
                else if (expr is Unknown huh)
                {
                    s = $"#{huh.Opcode:X2}";
                }
                else throw new Exception($"Unknown expression subclass {expr.GetType()}");
                if (IfFalse == FalseCond.ABORT) return $"AbortIfFalse({s})";
                return s;
            }
            private static readonly HashSet<string> eqs = new HashSet<string> { "==", "!=", "<=", ">=", ">", "<" };
            private static readonly Dictionary<string, int> commutes = new Dictionary<string, int>
            {
                ["+"] = 0,
                ["-"] = 0,
                ["*"] = 1,
                ["/"] = 1,
                ["&&"] = 2,
                ["||"] = 3,
            };

            public Expr Copy()
            {
                return Visit(previsit: e =>
                {
                    e = (Expr)e.MemberwiseClone();
                    if (e is FunctionCall f) f.Args = f.Args.ToList();
                    return e;
                });
            }
            public Expr Visit(Func<Expr, Expr> previsit = null, Func<Expr, Expr> postvisit = null)
            {
                Expr newArg = null;
                Expr preExpr = previsit?.Invoke(this);
                Expr expr = preExpr == null ? this : preExpr;
                if (expr is FunctionCall f)
                {
                    for (int i = 0; i < f.Args.Count; i++)
                    {
                        newArg = f.Args[i].Visit(previsit, postvisit);
                        if (newArg != null) f.Args[i] = newArg;
                    }
                }
                else if (expr is BinaryExpr b)
                {
                    newArg = b.Lhs.Visit(previsit, postvisit);
                    if (newArg != null) b.Lhs = newArg;
                    newArg = b.Rhs.Visit(previsit, postvisit);
                    if (newArg != null) b.Rhs = newArg;
                }
                else if (expr is UnaryExpr u)
                {
                    newArg = u.Arg.Visit(previsit, postvisit);
                    if (newArg != null) u.Arg = newArg;
                }
                Expr postExpr = postvisit?.Invoke(expr);
                if (postExpr != null) expr = postExpr;
                return preExpr == null && postExpr == null ? null : expr;
            }
        }

        public class ConstExpr : Expr
        {
            // Can be sbyte, float, double, int, string
            public object Value { get; set; }
            public override bool TryAsInt(out int o)
            {
                if (Value is sbyte sb)
                {
                    o = sb;
                    return true;
                }
                if (Value is int i)
                {
                    o = i;
                    return true;
                }
                o = 0;
                return false;
            }
            public override int GetHashCode() => Value.GetType().GetHashCode() ^ Value.ToString().GetHashCode();
            public override bool Equals(object obj) => obj is ConstExpr o && Equals(o);
            public bool Equals(ConstExpr o) => Value.Equals(o.Value);
        }
        public class FunctionCall : Expr
        {
            // Used to represent actual functions as well as built-in ops which can be written as functions
            // For real functions, expr is either the function name if known or f<number> if unknown.
            // Built-in functions:
            // SetReg[0-7](<expr>)
            // GetReg[0-7]()
            // StateGroupArg[<index>] (with brackets instead of parens for fun)
            public string Name { get; set; }
            public List<Expr> Args { get; set; }
        }
        public class BinaryExpr : Expr
        {
            // Supported ops: + - * / <= >= < > == != && ||
            public string Op { get; set; }
            public Expr Lhs { get; set; }
            public Expr Rhs { get; set; }
        }
        public class UnaryExpr : Expr
        {
            // Supported ops: N
            public string Op { get; set; }
            public Expr Arg { get; set; }
        }
        public class Unknown : Expr
        {
            public byte Opcode { get; set; }
        }
    }
}
