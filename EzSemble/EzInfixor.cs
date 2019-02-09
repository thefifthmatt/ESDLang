using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static SoulsFormats.ESD.EzSemble.Common;

namespace SoulsFormats.ESD.EzSemble
{
    public static partial class EzSembler
    {
        public class EzInfixor
        {
            private static bool IsFunction(EzSembleContext context, string s)
            {
                return s.StartsWith("f") || context.FunctionIDsByName.ContainsKey(s) || s.StartsWith("GetREG") || s.StartsWith("SetREG") || (s == "AbortIfFalse");
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
                //return exp;

                //if (Operators.Any(x => exp.Contains(x.Key)) || exp.Contains(" "))
                //    return $"({exp})";
                //else
                //    return exp;

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

            public static string BytecodeToInfix(EzSembleContext context, byte[] Bytes)
            {

                //string MEOWDEBUG_OLD_DISSEMBLE = MEOWDEBUG_OldDissemble(Bytes);

                Stack<string> stack = new Stack<string>();

                Queue<string> garbage = new Queue<string>();

                string popLastNonGarbageAndStoreGarbage(bool wantNumber = false)
                {
                    var popped = stack.Pop();
                    //while (popped == "~" || popped == ".")
                    //{
                    //    garbage.Enqueue(popped);
                    //    popped = stack.Pop();
                    //}

                    if (wantNumber)
                        return popped.Trim('(', ')');
                    else
                        return popped;
                }

                void restoreGarbage()
                {
                    while (garbage.Count > 0)
                        stack.Push(garbage.Dequeue());
                }

                for (int i = 0; i < Bytes.Length; i++)
                {
                    var b = Bytes[i];
                    if (b >= 0 && b <= 0x7F)
                    {
                        stack.Push($"{b - 64}");
                    }
                    else if (b == 0xA5)
                    {
                        int j = 0;
                        while (Bytes[i + j + 1] != 0 || Bytes[i + j + 2] != 0)
                            j += 2;
                        string text = Encoding.Unicode.GetString(Bytes, i + 1, j);
                        if (text.Contains('"') || text.Contains('\r') || text.Contains('\n'))
                            throw new Exception("Illegal character in string literal");
                        stack.Push($"\"{text}\"");
                        i += j + 2;
                    }
                    else if (b == 0x80)
                    {
                        stack.Push($"{BitConverter.ToSingle(Bytes, i + 1)}");
                        i += 4;
                    }
                    else if (b == 0x81)
                    {
                        stack.Push($"{BitConverter.ToDouble(Bytes, i + 1)}");
                        i += 8;
                    }
                    else if (b == 0x82)
                    {
                        stack.Push($"{BitConverter.ToInt32(Bytes, i + 1)}");
                        i += 4;
                    }
                    else if (b == 0x84)
                    {
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}()");
                    }
                    else if (b == 0x85)
                    {
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1})");
                    }
                    else if (b == 0x86)
                    {
                        var arg2 = popLastNonGarbageAndStoreGarbage();
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1}, {arg2})");
                    }
                    else if (b == 0x87)
                    {
                        var arg3 = popLastNonGarbageAndStoreGarbage();
                        var arg2 = popLastNonGarbageAndStoreGarbage();
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1}, {arg2}, {arg3})");
                    }
                    else if (b == 0x88)
                    {
                        var arg4 = popLastNonGarbageAndStoreGarbage();
                        var arg3 = popLastNonGarbageAndStoreGarbage();
                        var arg2 = popLastNonGarbageAndStoreGarbage();
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1}, {arg2}, {arg3}, {arg4})");
                    }
                    else if (b == 0x89)
                    {
                        var arg5 = popLastNonGarbageAndStoreGarbage();
                        var arg4 = popLastNonGarbageAndStoreGarbage();
                        var arg3 = popLastNonGarbageAndStoreGarbage();
                        var arg2 = popLastNonGarbageAndStoreGarbage();
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1}, {arg2}, {arg3}, {arg4}, {arg5})");
                    }
                    else if (b == 0x8A)
                    {
                        var arg6 = popLastNonGarbageAndStoreGarbage();
                        var arg5 = popLastNonGarbageAndStoreGarbage();
                        var arg4 = popLastNonGarbageAndStoreGarbage();
                        var arg3 = popLastNonGarbageAndStoreGarbage();
                        var arg2 = popLastNonGarbageAndStoreGarbage();
                        var arg1 = popLastNonGarbageAndStoreGarbage();
                        var id = popLastNonGarbageAndStoreGarbage(true);
                        restoreGarbage();
                        stack.Push($"{context.GetFunctionName(int.Parse(id))}({arg1}, {arg2}, {arg3}, {arg4}, {arg5}, {arg6})");
                    }
                    else if (OperatorsByByte.ContainsKey(b))
                    {
                        var item2 = popLastNonGarbageAndStoreGarbage();
                        var item1 = popLastNonGarbageAndStoreGarbage();

                        restoreGarbage();

                        stack.Push($"{GetExpressionWithParenthesesIfContainsOperator(item1, OperatorsByByte[b])} " +
                            $"{OperatorsByByte[b]} {GetExpressionWithParenthesesIfContainsOperator(item2, OperatorsByByte[b])}");
                    }
                    else if (b == 0xA6)
                    {
                        //if (stack.Count > 2)
                        //{
                        //    var stackContents = new string[stack.Count];
                        //    int j = stack.Count - 1;
                        //    while (stack.Count > 0)
                        //    {
                        //        var latest = stack.Pop();
                        //        stackContents[j] = latest;
                        //        j--;
                        //    }

                        //    stack.Push($"({string.Join(" ", stackContents)})");

                        //    Console.WriteLine("TEST");
                        //}
                        //else
                        //{
                        //    stack.Push($"({stack.Pop()})");
                        //}
                        stack.Push($"({stack.Pop()})");
                    }
                    else if (b >= 0xA7 && b <= 0xAE)
                    {
                        byte regIndex = (byte)(b - 0xA7);
                        var item = popLastNonGarbageAndStoreGarbage();
                        restoreGarbage();
                        stack.Push($"SetREG{regIndex}({item})");
                    }
                    else if (b >= 0xAF && b <= 0xB6)
                    {
                        byte regIndex = (byte)(b - 0xAF);
                        stack.Push($"GetREG{regIndex}()");
                    }
                    else if (b == 0xB7)
                    {
                        var item = stack.Pop();
                        stack.Push($"AbortIfFalse({item})");
                    }
                    else if (b == 0xA1)
                    {
                        //break;
                    }
                    else
                    {
                        stack.Push($"#{b:X2}");
                    }
                }

                return string.Join(" ", stack);
            }

            public static string InfixToPostFix(EzSembleContext context, string expression)
            {
                //expression = expression.Replace("\n", "~");

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
                            string thisText = "";

                            while (next < expression.Length && expression[next] != '"')
                                next++;

                            if (next == expression.Length)
                                throw new Exception("Unclosed string literal");

                            string value = expression.Substring(current + 1, next - current - 1);
                            if (value.Contains('\r') || value.Contains('\n'))
                                throw new Exception("String literals may not contain newlines");

                            stringSubstitutions.Add(value);
                            //expression = expression.Replace(value, $"{{{stringSubstitutions.Count - 1}}}");

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
                

                //string pattern = @"(?<=[^\\.a-zA-Z\\d])|(?=[^\\.a-zA-Z\\d])";
                string pattern = @"(?<=[-+*/(),^<>=&\|~])(?=.)|(?<=.)(?=[-+*/(),^<>=&\|~])";

                expression = expression.Replace(" ", "");
                Regex regExPattern = new Regex(pattern);
                List<string> expr = new List<string>(regExPattern.Split(expression));
                //expr.RemoveAll(s => String.IsNullOrEmpty(s.Trim()));

                //parse our expression and fix unary + and -
                ParseUnary(ref expr);

                //int continuationsQueued = 0;

                Stack<int> funcArgCounts = new Stack<int>();

                bool popAndEnqueue(bool rightParenthesis = false)
                {
                    var popped = stack.Pop();
                    if (IsFunction(context, popped))
                    {
                        //Queue<string> garbage = new Queue<string>();
                        //while (queue[queue.Count - 1] == "~")
                        //{
                        //    garbage.Enqueue(queue[queue.Count - 1]);
                        //    queue.RemoveAt(queue.Count - 1);
                        //}

                        var argCount = funcArgCounts.Pop();

                        if (popped.StartsWith("SetREG"))
                        {
                            queue.Add($">[{popped.Substring(popped.Length - 1, 1)}]");

                            //var argCount = int.Parse(queue[queue.Count - 1]);
                            //queue.RemoveAt(queue.Count - 1);

                            //if (argCount == 1)
                            //{
                            //    queue.Add($">[{popped.Substring(popped.Length - 1, 1)}]");
                            //}
                            //else
                            //{
                            //    throw new Exception("SetREG must be passed exactly 1 argument.");
                            //}
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
                        else
                        {
                            //queue.RemoveAt(queue.Count - 1);

                            queue.Add($"({argCount})");
                        }

                        //while (garbage.Count > 0)
                        //    queue.Add(garbage.Dequeue());
                        return true;
                    }
                    else
                    {
                        queue.Add(popped);
                        //if (rightParenthesis)
                        //{
                        //    queue.Add("~");
                        //}
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
                    //if (s == "~")
                    //{
                    //    continuationsQueued++;
                    //    //queue[queue.Count - 1] += "~";
                    //    //queue.Add("~");
                    //}
                    //else 
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
                    else if (s.StartsWith("GetREG") || s.StartsWith("SetREG") || s == "AbortIfFalse")
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
                    else if (s == "(")
                    {
                        stack.Push(s);
                    }

                    //handle closing parenthesis
                    //pop all operators off the stack until the matching 
                    //opening parenthesis is found and then discard the
                    //opening parenthesis
                    else if (s == ")")
                    {
                        while (stack.Count != 0 && stack.Peek() != "(")
                        {
                            if (!popAndEnqueue(rightParenthesis: true))
                            {
                                queue.Add("~");
                            }
                        }

                        //if (funcArgCounts.Count > 0)
                        //    queue.Add($"{funcArgCounts.Pop()}");
                        //forget the (
                        stack.Pop();
                    }

                    //do we have an argument separator, if so, pop everything off the stack
                    //until we reach the opening parenthesis, but leave that on the stack
                    else if (s == ",")
                    {
                        while (stack.Peek() != "(")
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
