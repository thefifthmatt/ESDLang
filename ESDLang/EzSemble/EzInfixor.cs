using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static ESDLang.EzSemble.AST;
using static ESDLang.EzSemble.Common;

namespace ESDLang.EzSemble
{
    public static partial class EzSembler
    {
        public class EzInfixor
        {
            private static bool IsFunction(EzSembleContext context, string s)
            {
                return s.StartsWith("f") || context.FunctionIDsByName.ContainsKey(s) || s.StartsWith("GetREG") || s.StartsWith("SetREG") || s == "AbortIfFalse" || s == "StateGroupArg";
            }

            //Get the precedence of the operator/function passed in
            private static int GetPrecedence(EzSembleContext context, string s)
            {
                int max = 0;
                //if the passed is a function, make it the highest precedence
                //we simply get the max precedence value for all maths operators and add 1

                if (IsFunction(context, s))
                    max = Math.Max(Operators[Operators.Keys.First()][0], Operators[Operators.Keys.Last()][0]) + 1;
                else
                    max = Operators[s][0];

                return max;
            }

            //Get the association of the operator passed in
            private static int GetAssociation(string s)
            {
                return Operators[s][1];
            }

            private static void ParseUnary(ref List<string> expr)
            {
                for (int i = 0; i < expr.Count; i++)
                {
                    //we have a minus
                    //if its a unary, then the following happens:
                    //1. At the beginning: -1 * 2 = ( 0 - 1 ) * 2
                    //2. After an opening parenthesis: 1 + ( -2 * 3 ) = 1 + ( ( 0 - 2 ) * 3 )
                    //3. After an operator: 1 + -2 = 1 + ( 0 - 2 )
                    if (expr[i] == "-")
                    {
                        if (i == expr.Count - 1)
                        {
                            throw new Exception("Infix expression has a minus sign at the very end.");
                        }
                        else
                        {
                            //is it at the beginning of the expression OR
                            //it follows and opening parenthesis OR operator>
                            //if so, its a unary minus
                            if (i == 0 || expr[i - 1] == "(" || Operators.ContainsKey(expr[i - 1]))
                            {
                                expr[i] = expr[i] + expr[i + 1];
                                expr.RemoveAt(i + 1);
                            }
                        }

                    }
                    ////we have a +
                    //else if (expr[i] == "+")
                    //{
                    //    //is it at the beginning of the expression
                    //    //OR it follows an opening parenthesis OR operator?
                    //    //if so, we can drop it, as it serves no purpose
                    //    if (i == 0 || expr[i - 1] == "(" || Operators.ContainsKey(expr[i - 1]))
                    //        expr.RemoveAt(i);
                    //}
                    else if (i > 0 && expr[i] == "=" && expr[i - 1] == "=")
                    {
                        expr[i - 1] = "==";
                        expr.RemoveAt(i);
                        i--;
                    }
                    else if (i > 0 && expr[i] == "=" && expr[i - 1] == ">")
                    {
                        expr[i - 1] = ">=";
                        expr.RemoveAt(i);
                        i--;
                    }
                    else if (i > 0 && expr[i] == "=" && expr[i - 1] == "<")
                    {
                        expr[i - 1] = "<=";
                        expr.RemoveAt(i);
                        i--;
                    }
                    else if (i > 0 && expr[i] == "=" && expr[i - 1] == "!")
                    {
                        expr[i - 1] = "!=";
                        expr.RemoveAt(i);
                        i--;
                    }
                    else if (i > 0 && expr[i] == "|" && expr[i - 1] == "|")
                    {
                        expr[i - 1] = "||";
                        expr.RemoveAt(i);
                        i--;
                    }
                    else if (i > 0 && expr[i] == "&" && expr[i - 1] == "&")
                    {
                        expr[i - 1] = "&&";
                        expr.RemoveAt(i);
                        i--;
                    }
                }
            }

            private static Dictionary<string, int[]> Operators = new Dictionary<string, int[]>
            {
                { "^", new int[] { 5, 1 } },
                { "*", new int[] { 4, 0 } },
                { "/", new int[] { 4, 0 } },
                { "+", new int[] { 3, 0 } },
                { "-", new int[] { 3, 0 } },
                { "<", new int[] { 2, 0 } },
                { ">", new int[] { 2, 0 } },
                { "==", new int[] { 2, 0 } },
                { "!=", new int[] { 2, 0 } },
                { ">=", new int[] { 2, 0 } },
                { "<=", new int[] { 2, 0 } },
                { "&&", new int[] { 1, 0 } },
                { "||", new int[] { 1, 0 } },
            };

            private static string GetExpressionWithParenthesesIfContainsOperator(string exp, string op)
            {
                if (op == "&&" || op == "||")
                {
                    if (exp.Contains("&&") || exp.Contains("||"))
                        return $"({exp})";
                    else
                        return exp;
                }
                else
                {
                    if (Operators.Any(x => exp.Contains(x.Key)) || exp.Contains(" "))
                        return $"({exp})";
                    else
                        return exp;
                }

            }

            public static Expr BytecodeToInfix(EzSembleContext context, byte[] Bytes)
            {
                var bigEndianReverseBytes = Bytes.Reverse().ToArray();

                Stack<Expr> exprs = new Stack<Expr>();
                List<Expr> popArgs(int amount)
                {
                    List<Expr> args = new List<Expr>();
                    for (int i = 0; i < amount; i++)
                    {
                        args.Add(exprs.Pop());
                    }
                    args.Reverse();
                    return args;
                }

                for (int i = 0; i < Bytes.Length; i++)
                {
                    var b = Bytes[i];
                    if (b >= 0 && b <= 0x7F)
                    {
                        exprs.Push(new ConstExpr { Value = (sbyte)(b - 64) });
                    }
                    else if (b == 0xA5)
                    {
                        int j = 0;
                        while (Bytes[i + j + 1] != 0 || Bytes[i + j + 2] != 0)
                            j += 2;
                        string text = context.IsBigEndian ?
                            Encoding.BigEndianUnicode.GetString(Bytes, i + 1, j)
                            : Encoding.Unicode.GetString(Bytes, i + 1, j);

                        if (text.Contains('"') || text.Contains('\r') || text.Contains('\n'))
                            throw new Exception("Illegal character in string literal");
                        exprs.Push(new ConstExpr { Value = text });
                        i += j + 2;
                    }
                    else if (b == 0x80)
                    {
                        float val;
                        if (!context.IsBigEndian)
                        {
                            val = BitConverter.ToSingle(Bytes, i + 1);
                        }
                        else
                        {
                            val = BitConverter.ToSingle(bigEndianReverseBytes, (bigEndianReverseBytes.Length - 1) - (i + 1) - 4);
                        }
                        exprs.Push(new ConstExpr { Value = val });

                        i += 4;
                    }
                    else if (b == 0x81)
                    {
                        double val;
                        if (!context.IsBigEndian)
                        {
                            val = BitConverter.ToDouble(Bytes, i + 1);
                        }
                        else
                        {
                            val = BitConverter.ToDouble(bigEndianReverseBytes, (bigEndianReverseBytes.Length - 1) - (i + 1) - 8);
                        }
                        exprs.Push(new ConstExpr { Value = val });

                        i += 8;
                    }
                    else if (b == 0x82)
                    {
                        int val;
                        if (!context.IsBigEndian)
                        {
                            val = BitConverter.ToInt32(Bytes, i + 1);
                        }
                        else
                        {
                            val = BitConverter.ToInt32(bigEndianReverseBytes, (bigEndianReverseBytes.Length - 1) - (i + 1) - 4);
                        }
                        exprs.Push(new ConstExpr { Value = val });

                        i += 4;
                    }
                    else if (b == 0x84)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(0), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x85)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(1), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x86)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(2), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x87)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(3), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x88)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(4), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x89)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(5), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (b == 0x8A)
                    {
                        exprs.Push(new FunctionCall { Args = popArgs(6), Name = context.GetFunctionInfo(exprs.Pop().AsInt()).Name });
                    }
                    else if (OperatorsByByte.ContainsKey(b))
                    {
                        if (OperatorsByByte[b] == "N")
                        {
                            exprs.Push(new UnaryExpr { Op = "N", Arg = exprs.Pop() });
                        }
                        else
                        {
                            exprs.Push(new BinaryExpr { Op = OperatorsByByte[b], Rhs = exprs.Pop(), Lhs = exprs.Pop() });
                        }
                    }
                    else if (b == 0xA6)
                    {
                        Expr top = exprs.Peek();
                        top.IfFalse = FalseCond.CONTINUE;
                    }
                    else if (b >= 0xA7 && b <= 0xAE)
                    {
                        byte regIndex = (byte)(b - 0xA7);
                        exprs.Push(new FunctionCall { Args = popArgs(1), Name = $"SetREG{regIndex}" });
                    }
                    else if (b >= 0xAF && b <= 0xB6)
                    {
                        byte regIndex = (byte)(b - 0xAF);
                        exprs.Push(new FunctionCall { Args = popArgs(0), Name = $"GetREG{regIndex}" });
                    }
                    else if (b == 0xB7)
                    {
                        Expr top = exprs.Peek();
                        top.IfFalse = FalseCond.ABORT;
                    }
                    else if (b == 0xB8)
                    {
                        // exprs.Push(new FunctionCall { Args = popArgs(1), Name = "StateGroupArg" });
                        FunctionCall func = new FunctionCall { Args = popArgs(1), Name = "StateGroupArg" };
                        ConstExpr ce = func.Args[0] as ConstExpr;
                        // Console.WriteLine($"{ce} {ce.Value.GetType()}");
                        exprs.Push(func);
                    }
                    else if (b == 0xB9)
                    {
                        exprs.Push(new CallResult());
                    }
                    else if (b == 0xBA)
                    {
                        // This opcode just returns a constant value 0x7FFFFFFF
                        // But use higher-level representation of it
                        exprs.Push(new CallOngoing());
                    }
                    else if (b == 0xA1)
                    {
                        //break;
                    }
                    else
                    {
                        exprs.Push(new Unknown { Opcode = b });
                    }
                }
                if (exprs.Count != 1) throw new Exception("Could not parse expr. Remaining stack: " + string.Join("; ", exprs) + $"; = {string.Join(" ", Bytes.Select(x => x.ToString("X2")))}");
                return exprs.Pop();
            }

            public static string InfixToEzLanguage(EzSembleContext context, string expression)
            {
                List<string> queue = new List<string>();
                Stack<string> stack = new Stack<string>();

                List<string> stringSubstitutions = new List<string>();

                if (expression.Contains("\""))
                {
                    int current = 0;
                    int next = current + 1;

                    while (current < expression.Length)
                    {
                        next = current + 1;

                        if (expression[current] == '"')
                        {
                            while (next < expression.Length && expression[next] != '"')
                                next++;

                            if (next == expression.Length)
                                throw new Exception("Unclosed string literal");

                            string value = expression.Substring(current + 1, next - current - 1);
                            if (value.Contains('\r') || value.Contains('\n'))
                                throw new Exception("String literals may not contain newlines");

                            stringSubstitutions.Add(value);

                            next++;
                        }

                        current = next;
                    }

                    for (int i = 0; i < stringSubstitutions.Count; i++)
                    {
                        expression = expression.Replace(stringSubstitutions[i], $"{{{i}}}");
                    }
                }

                //populate operators
                //int format is {precedence, association -> 0=Left 1=Right}

                string pattern = @"(?<=[-+*/(),^<>=&\|~!\[\]])(?=.)|(?<=.)(?=[-+*/(),^<>=&\|~!\[\]])";


                expression = expression.Replace(" ", "");
                Regex regExPattern = new Regex(pattern);
                List<string> expr = new List<string>(regExPattern.Split(expression));

                //parse our expression and fix unary + and -
                ParseUnary(ref expr);

                Stack<int> funcArgCounts = new Stack<int>();

                bool popAndEnqueue()
                {
                    var popped = stack.Pop();
                    if (IsFunction(context, popped))
                    {
                        var argCount = funcArgCounts.Pop();

                        if (popped.StartsWith("SetREG"))
                        {
                            queue.Add($">[{popped.Substring(popped.Length - 1, 1)}]");
                        }
                        else if (popped.StartsWith("GetREG"))
                        {
                            queue.Add($"[{popped.Substring(popped.Length - 1, 1)}]>");
                        }
                        else if (popped == "AbortIfFalse")
                        {
                            if (queue.Count == 0 || argCount != 1)
                                throw new Exception("Invalid AbortIfFalse call");

                            queue.Add($".");
                        }
                        else if (popped == "StateGroupArg")
                        {
                            if (queue.Count == 0 || argCount != 1)
                                throw new Exception("Invalid StateGroupArg call");

                            queue.Add($"#B8");
                        }
                        else
                        {
                            queue.Add($"({argCount})");
                        }
                        return true;
                    }
                    else
                    {
                        queue.Add(popped);
                        return false;
                    }
                }

                void registArgument()
                {
                    if (funcArgCounts.Count > 0 && funcArgCounts.Peek() == 0)
                        funcArgCounts.Push(funcArgCounts.Pop() + 1);
                }

                foreach (var s in expr)
                {
                    if (Operators.ContainsKey(s))
                    {
                        //while the stack is not empty and the top of the stack is not an (
                        while (stack.Count > 0 && stack.Peek() != "(")
                        {
                            if ((GetAssociation(s) == 0 && GetPrecedence(context, s) <= GetPrecedence(context, stack.Peek())) ||
                                (GetAssociation(s) == 1 && GetPrecedence(context, s) < GetPrecedence(context, stack.Peek()))
                              )
                                popAndEnqueue();
                            else
                                break;
                        }

                        //push operator onto the stack
                        stack.Push(s);
                    }
                    //These things aren't technically functions and thus do not 
                    //need to push their ID as an expression.
                    else if (s.StartsWith("GetREG") || s.StartsWith("SetREG") || s == "AbortIfFalse" || s == "StateGroupArg")
                    {
                        registArgument();
                        stack.Push(s);
                        funcArgCounts.Push(0);
                    }
                    //is our token on our defined functions
                    else if (IsFunction(context, s))
                    {
                        registArgument();
                        stack.Push(s);
                        queue.Add(context.GetFunctionID(s).ToString());
                        funcArgCounts.Push(0);
                    }

                    //handle opening parenthesis
                    //simply push this on the stack
                    else if (s == "(" || s == "[")
                    {
                        stack.Push("(");
                    }

                    //handle closing parenthesis
                    //pop all operators off the stack until the matching 
                    //opening parenthesis is found and then discard the
                    //opening parenthesis
                    else if (s == ")" || s == "]")
                    {
                        while (stack.Count != 0 && stack.Peek() != "(" && stack.Peek() != "[")
                        {
                            // This is where we'd add ContinueIfFalse if we cared about it.
                            popAndEnqueue();
                        }

                        //forget the (
                        stack.Pop();
                    }

                    //do we have an argument separator, if so, pop everything off the stack
                    //until we reach the opening parenthesis, but leave that on the stack
                    else if (s == ",")
                    {
                        while (stack.Peek() != "(" && stack.Peek() != "[")
                            popAndEnqueue();
                        funcArgCounts.Push(funcArgCounts.Pop() + 1);
                    }
                    else
                    {
                        //none of the above so queue it
                        registArgument();
                        queue.Add(s);
                    }
                }

                //pop off the rest of the stack
                while (stack.Count != 0)
                    popAndEnqueue();

                var resultExpr = string.Join(" ", queue);

                for (int i = 0; i < stringSubstitutions.Count; i++)
                {
                    resultExpr = resultExpr.Replace($"{{{i}}}", stringSubstitutions[i]);
                }

                if (resultExpr == "GetStateChangeType 233")
                    throw new Exception();
                return resultExpr;

            }
        }
    }
}
