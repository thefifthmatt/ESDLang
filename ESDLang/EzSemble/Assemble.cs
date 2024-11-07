using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Text;
using SoulsFormats;
using static ESDLang.EzSemble.AST;
using static ESDLang.EzSemble.Common;
using System.Text.RegularExpressions;
using ESDLang.Doc;

namespace ESDLang.EzSemble
{
    /// <summary>
    /// Assembles and dissembles "EzLanguage" bytecode.
    /// </summary>
    public static partial class EzSembler
    {
        /// <summary>
        /// Assembles a plain text "EzLanguage" command call into a CommandCall object.
        /// </summary>
        public static ESD.CommandCall AssembleCommandCall(EzSembleContext context, string plaintext)
        {
            var regex = System.Text.RegularExpressions.Regex.Match(plaintext, @"^([A-Za-z0-9_\-:]+)\((.*)\)$");

            if (regex.Groups.Count != 3)
            {
                throw new Exception($"Invalid EzLanguage command call text: \"{plaintext}\"");
            }

            var command = regex.Groups[1].Value;
            var cmdId = context.GetCommandID(command);
            var argsText = regex.Groups[2].Value.Trim();

            var finalArgs = new List<string>();

            if (!string.IsNullOrWhiteSpace(argsText))
            {
                // If <= 2 chars theres no way there can be more than 1 arg
                // And obviously if there's no commas
                if (argsText.Length <= 2 || !argsText.Contains(","))
                {
                    finalArgs = new List<string>() { argsText };
                }
                else
                {
                    int thisArgStartIndex = 0;
                    int innerParenthesisLevel = 0;
                    for (int i = 0; i < argsText.Length; i++)
                    {
                        if (i < argsText.Length - 1)
                        {
                            if (argsText[i] == '(')
                            {
                                innerParenthesisLevel++;
                            }
                            else if (argsText[i] == ')')
                            {
                                if (innerParenthesisLevel > 0)
                                    innerParenthesisLevel--;
                                else
                                    throw new Exception("Extra parenthesis found in command call args.");
                            }

                            if (argsText[i] == ',')
                            {
                                if (innerParenthesisLevel == 0)
                                {
                                    finalArgs.Add(argsText.Substring(thisArgStartIndex, i - thisArgStartIndex));
                                    thisArgStartIndex = i + 1;
                                }
                            }
                        }
                        else //Very last char
                        {
                            if (argsText[i] == ',' || argsText[i] == '(')
                            {
                                throw new Exception("Very last char in command args cannot be a '(' or ','");
                            }
                            else if (argsText[i] == ')')
                            {
                                if (innerParenthesisLevel > 0)
                                    innerParenthesisLevel--;
                                else
                                    throw new Exception("Extra parenthesis found in command call args.");
                            }
                        }
                    }

                    if (thisArgStartIndex < argsText.Length - 1)
                    {
                        finalArgs.Add(argsText.Substring(thisArgStartIndex, (argsText.Length) - thisArgStartIndex));
                    }

                    if (innerParenthesisLevel != 0)
                    {
                        throw new Exception("Unclosed parenthesis found in command call args.");
                    }
                }
            }

            return new ESD.CommandCall()
            {
                CommandBank = cmdId.Bank,
                CommandID = cmdId.ID,
                Arguments = finalArgs.Select(x => AssembleExpression(context, x)).ToList(),
            };
        }

        public static List<ESD.CommandCall> AssembleCommandScript(EzSembleContext context, string plaintext)
        {
            var result = new List<ESD.CommandCall>();
            foreach (var cmdTxt in plaintext.Split(';').Select(x =>
            {
                var cmdLine = x.Replace("\r", "").Trim(' ', '\n');
                if (cmdLine.Contains("//"))
                {
                    cmdLine = cmdLine.Substring(0, cmdLine.IndexOf("//"));
                }
                return cmdLine;
            }).Where(x => !string.IsNullOrWhiteSpace(x)))
            {
                result.Add(AssembleCommandCall(context, cmdTxt.Replace("\n", "")));
            }
            return result;
        }

        private static (int, int) ParseCommandID(string name)
        {
            // With ESDDocumentation, this format is no longer necessary, but may require a FunctionCall rewrite to eradicate entirely
            var regex = Regex.Match(name, @"(\d+):(-?\d+)");
            if (regex.Groups.Count == 3
                && int.TryParse(regex.Groups[1].Value, out int cmdBank)
                && int.TryParse(regex.Groups[2].Value, out int cmdID))
            {
                return (cmdBank, cmdID);
            }
            else
            {
                throw new Exception($"Command name '{name}' does not exist in loaded documentation and" +
                    $" couldn't be parsed as a <Bank>:<ID>() representation of the command.");
            }
        }

        private static int ParseFunctionID(string name)
        {
            if (name.StartsWith("f") && int.TryParse(name.Substring(1), out int funcID))
            {
                return funcID;
            }
            else
            {
                throw new Exception($"Function name '{name}' does not exist in the loaded documentation and" +
                    $" couldn't be parsed as a f<ID>() representation of the function.");
            }
        }

        public static List<ESD.CommandCall> AssembleCommandScript(EzSembleContext context, Block block)
        {
            var result = new List<ESD.CommandCall>();
            foreach (Statement st in block.Cmds)
            {
                if (EzSembleContext.UseNew)
                {
                    int bank, id;
                    if (context.Doc.CommandsByName.TryGetValue(st.Name, out ESDDocumentation.MethodDoc methodDoc))
                    {
                        bank = methodDoc.Bank;
                        id = methodDoc.ID;
                    }
                    else
                    {
                        (bank, id) = ParseCommandID(st.Name);
                    }
                }
                else
                {
                    (int bank, int id) = context.GetCommandID(st.Name);
                    result.Add(new ESD.CommandCall()
                    {
                        CommandBank = bank,
                        CommandID = id,
                        Arguments = st.Args.Select(x => AssembleExpression(context, x)).ToList(),
                    });
                }
            }
            return result;
        }

        public static byte[] AssembleExpression(EzSembleContext context, Expr topExpr)
        {
            using (var ms = new MemoryStream())
            using (var bw = new BinaryWriter(ms, Encoding.Unicode))
            {
                void writeExpr(Expr expr)
                {
                    // Number
                    if (expr is ConstExpr ce)
                    {
                        if (ce.Value is int i)
                        {
                            bw.Write((byte)0x82);
                            bw.Write(i);
                        }
                        else if (ce.Value is sbyte b)
                        {
                            bw.Write((byte)(b + 64));
                        }
                        else if (ce.Value is float f)
                        {
                            bw.Write((byte)0x80);
                            bw.Write(f);
                        }
                        else if (ce.Value is double d)
                        {
                            bw.Write((byte)0x81);
                            bw.Write(d);
                        }
                        else if (ce.Value is string s)
                        {
                            if (s.Contains('\r') || s.Contains('\n'))
                                throw new Exception("String literals may not contain newlines");
                            bw.Write((byte)0xA5);
                            bw.Write(Encoding.Unicode.GetBytes(s + "\0"));
                        }
                        else throw new Exception($"Invalid type {ce.Value.GetType()} for ConstExpr {ce} in {topExpr}");
                    }
                    else if (expr is UnaryExpr ue)
                    {
                        writeExpr(ue.Arg);
                        bw.Write(BytesByOperator[ue.Op]);
                    }
                    else if (expr is BinaryExpr be)
                    {
                        writeExpr(be.Lhs);
                        writeExpr(be.Rhs);
                        bw.Write(BytesByOperator[be.Op]);
                    }
                    else if (expr is FunctionCall func)
                    {
                        string name = func.Name;
                        if (name.StartsWith("SetREG"))
                        {
                            int regIndex = byte.Parse(name.Substring(name.Length - 1));
                            writeExpr(func.Args[0]);
                            bw.Write((byte)(0xA7 + regIndex));
                        }
                        else if (name.StartsWith("GetREG"))
                        {
                            int regIndex = byte.Parse(name.Substring(name.Length - 1));
                            bw.Write((byte)(0xAF + regIndex));
                        }
                        else if (name.StartsWith("StateGroupArg"))
                        {
                            int index = func.Args[0].AsInt();
                            bw.Write((byte)(index + 64));
                            bw.Write((byte)0xB8);
                        }
                        else
                        {
                            int id;
                            if (EzSembleContext.UseNew)
                            {
                                if (context.Doc.FunctionsByName.TryGetValue(name, out ESDDocumentation.MethodDoc methodDoc))
                                {
                                    id = methodDoc.ID;
                                }
                                else
                                {
                                    id = ParseFunctionID(name);
                                }
                            }
                            else
                            {
                                id = context.GetFunctionID(name);
                            }
                            if (id >= -64 && id <= 63)
                            {
                                bw.Write((byte)(id + 64));
                            }
                            else
                            {
                                bw.Write((byte)0x82);
                                bw.Write(id);
                            }
                            // for (int i = func.Args.Count - 1; i >= 0; i--)
                            for (int i = 0; i < func.Args.Count; i++)
                            {
                                writeExpr(func.Args[i]);
                            }
                            bw.Write((byte)(0x84 + func.Args.Count));
                        }
                    }
                    else if (expr is CallResult)
                    {
                        bw.Write((byte)0xB9);
                    }
                    else if (expr is CallOngoing)
                    {
                        bw.Write((byte)0xBA);
                    }
                    else if (expr is Unknown huh)
                    {
                        bw.Write(huh.Opcode);
                    }
                    else throw new Exception($"Unknown expression subclass {expr.GetType()}: {expr} in {topExpr}");
                    if (expr.IfFalse == FalseCond.CONTINUE)
                    {
                        bw.Write(BytesByTerminator['~']);
                    }
                    else if (expr.IfFalse == FalseCond.ABORT)
                    {
                        bw.Write(BytesByTerminator['.']);
                    }
                }
                writeExpr(topExpr);
                bw.Write((byte)0xA1);
                byte[] arr = ms.ToArray();
                if (arr.Length == 1) throw new Exception($"{topExpr}");
                return arr;
            }
        }

        /// <summary>
        /// Assembles a plain text "EzLanguage" expression into bytecode.
        /// </summary>
        public static byte[] AssembleExpression(EzSembleContext context, string plaintext)
        {
            var postfixPlaintext = EzInfixor.InfixToEzLanguage(context, plaintext);
            using (var ms = new MemoryStream())
            using (var bw = new BinaryWriter(ms, Encoding.Unicode))
            {
                int current = 0;
                int next = 0;

                while (current < postfixPlaintext.Length)
                {
                    next = current + 1;
                    Parse(postfixPlaintext, bw, current, ref next);
                    current = next;
                }

                bw.Write((byte)0xA1);
                return ms.ToArray();
            }
        }

        private static void Parse(string plaintext, BinaryWriter bw, int current, ref int next)
        {
            if (current == 0 && plaintext[current] == '.')
                throw new Exception("Cannot start with an abort if previous number is false byte");
            else if (current == 0 && plaintext[current] == '~')
                throw new Exception("Cannot start with a continuation byte thing or whatever");

            // Number literal
            if (plaintext[current] == '-' || char.IsDigit(plaintext[current]))
            {
                // Is subtract and not a literal
                if (plaintext[current] == '-' && (next == plaintext.Length || !char.IsDigit(plaintext[next])))
                {
                    bw.Write(BytesByOperator["-"]);
                }
                else
                {
                    while (next < plaintext.Length && char.IsDigit(plaintext[next]))
                        next++;

                    if (next + 1 < plaintext.Length && plaintext[next] == '.' && char.IsDigit(plaintext[next + 1]))
                    {
                        next++;
                        while (next < plaintext.Length && char.IsDigit(plaintext[next]))
                            next++;
                    }

                    string str = plaintext.Substring(current, next - current);
                    double value = double.Parse(str);
                    if (value == Math.Floor(value))
                    {
                        if (value >= -64 && value <= 63)
                        {
                            bw.Write((byte)(value + 64));
                        }
                        else
                        {
                            bw.Write((byte)0x82);
                            bw.Write((int)value);
                        }
                    }
                    else if (value == (float)value)
                    {
                        bw.Write((byte)0x80);
                        bw.Write((float)value);
                    }
                    else
                    {
                        bw.Write((byte)0x81);
                        bw.Write(value);
                    }
                }
               
            }
            // String literal
            else if (plaintext[current] == '"')
            {
                while (next < plaintext.Length && plaintext[next] != '"')
                    next++;

                if (next == plaintext.Length)
                    throw new Exception("Unclosed string literal");

                string value = plaintext.Substring(current + 1, next - current - 1);
                if (value.Contains('\r') || value.Contains('\n'))
                    throw new Exception("String literals may not contain newlines");

                bw.Write((byte)0xA5);
                bw.Write(Encoding.Unicode.GetBytes(value + "\0"));

                next++;
            }
            // Add
            else if (plaintext[current] == '+')
            {
                bw.Write(BytesByOperator["+"]);
            }
            // Multiply
            else if (plaintext[current] == '*')
            {
                bw.Write(BytesByOperator["*"]);
            }
            // Negate
            else if (plaintext[current] == 'N' || plaintext[current] == 'n')
            {
                bw.Write(BytesByOperator["N"]);
            }
            else if (plaintext[current] == '/')
            {
                // Comment
                if (next < plaintext.Length && plaintext[next] == '/')
                {
                    while (next < plaintext.Length && plaintext[next] != '\n')
                        next++;
                    next++;
                }
                // Divide
                else
                {
                    bw.Write(BytesByOperator["/"]);
                }
            }
            else if (plaintext[current] == '<')
            {
                // Less than or equal to
                if (next < plaintext.Length && plaintext[next] == '=')
                {
                    bw.Write(BytesByOperator["<="]);
                    next++;
                }
                // Less than
                else
                {
                    bw.Write(BytesByOperator["<"]);
                }
            }
            else if (plaintext[current] == '>')
            {
                // Set register
                if (next < plaintext.Length && plaintext[next] == '[')
                {
                    if (next + 2 >= plaintext.Length || plaintext[next + 2] != ']')
                        throw new Exception("Malformed register storage");
                    if (!"01234567".Contains(plaintext[next + 1]))
                        throw new Exception("Register must be from 0-7");

                    bw.Write((byte)(0xA7 + byte.Parse(plaintext[next + 1].ToString())));
                    next += 3;
                }
                // Greater than or equal to
                else if (next < plaintext.Length && plaintext[next] == '=')
                {
                    bw.Write(BytesByOperator[">="]);
                    next++;
                }
                // Greater than
                else
                {
                    bw.Write(BytesByOperator[">"]);
                }
            }
            // Equal to
            else if (plaintext[current] == '=')
            {
                if (next == plaintext.Length || plaintext[next] != '=')
                    throw new Exception("Orphaned = found");

                bw.Write(BytesByOperator["=="]);
                next++;
            }
            // Not equal to
            else if (plaintext[current] == '!')
            {
                if (next == plaintext.Length || plaintext[next] != '=')
                    throw new Exception("Orphaned ! found");

                bw.Write(BytesByOperator["!="]);
                next++;
            }
            // Logical and
            else if (plaintext[current] == '&')
            {
                if (next == plaintext.Length || plaintext[next] != '&')
                    throw new Exception("Orphaned & found");

                bw.Write(BytesByOperator["&&"]);
                next++;
            }
            // Logical or
            else if (plaintext[current] == '|')
            {
                if (next == plaintext.Length || plaintext[next] != '|')
                    throw new Exception("Orphaned | found");

                bw.Write(BytesByOperator["||"]);
                next++;
            }
            // Function call
            else if (plaintext[current] == '(')
            {
                if (next + 1 >= plaintext.Length || plaintext[next + 1] != ')')
                    throw new Exception("Unclosed function call");
                if (!"0123456".Contains(plaintext[next]))
                    throw new Exception("Function call must take 0-6 arguments");

                bw.Write((byte)(0x84 + byte.Parse(plaintext[next].ToString())));
                next += 2;
            }
            // Get register
            else if (plaintext[current] == '[')
            {
                if (next + 2 >= plaintext.Length || plaintext[next + 1] != ']' || plaintext[next + 2] != '>')
                    throw new Exception("Malformed register retrieval");
                if (!"01234567".Contains(plaintext[next]))
                    throw new Exception("Register must be from 0-7");

                bw.Write((byte)(0xAF + byte.Parse(plaintext[next].ToString())));
                next += 3;
            }
            // ~ or .
            else if (BytesByTerminator.ContainsKey(plaintext[current]))
            {
                bw.Write(BytesByTerminator[plaintext[current]]);
            }
            // Unknown opcode
            else if (plaintext[current] == '#')
            {
                if (next + 1 >= plaintext.Length)
                    throw new Exception("Hex literal too short");

                bw.Write(Convert.ToByte(plaintext.Substring(current + 1, 2), 16));
                next += 2;
            }
            // Whitespace
            else if (char.IsWhiteSpace(plaintext[current]))
            {
                while (next < plaintext.Length && char.IsWhiteSpace(plaintext[next]))
                    next++;
            }
            // Uh-oh
            else
            {
                throw new Exception($"Unknown character: {plaintext[current]}");
            }
        }
    }
}
