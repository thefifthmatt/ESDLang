using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using static SoulsFormats.ESD.EzSemble.Common;

namespace SoulsFormats.ESD.EzSemble
{
    public static partial class EzSembler
    {
        /// <summary>
        /// Dissembles a CommandCall object into a line of "EzLanguage" plain text.
        /// </summary>
        public static string DissembleCommandCall(SoulsFormats.ESD.ESD.CommandCall c)
        {
            return $"{c.CommandBank}:{c.CommandID}({string.Join(", ", c.Arguments)})";
        }

        /// <summary>
        /// Dissembles a list of CommandCall objects into a plain text "EzLanguage" script.
        /// </summary>
        public static string DissembleCommandScript(List<SoulsFormats.ESD.ESD.CommandCall> script)
        {
            return string.Join("\n", script.Select(x => $"{DissembleCommandCall(x)};"));
        }

        //public static string MEOWDEBUG_OldDissemble(byte[] bytes)
        //{
        //    if (bytes.Last() != 0xA1)
        //        throw new Exception("All evaluators must end with 0xA1");

        //    var sb = new StringBuilder();
        //    bool newline = true;

        //    for (int i = 0; i < bytes.Length - 1; i++)
        //    {
        //        byte b = bytes[i];
        //        if (TerminatorsByByte.ContainsKey(b))
        //        {
        //            newline = true;
        //            sb.Append(TerminatorsByByte[b]);
        //        }
        //        else
        //        {
        //            if (newline)
        //                newline = false;
        //            else
        //                sb.Append(" ");

        //            if (b >= 0 && b <= 0x7F)
        //            {
        //                sb.Append($"{b - 64}");
        //            }
        //            else if (b == 0xA5)
        //            {
        //                int j = 0;
        //                while (bytes[i + j + 1] != 0 || bytes[i + j + 2] != 0)
        //                    j += 2;
        //                string text = Encoding.Unicode.GetString(bytes, i + 1, j);
        //                if (text.Contains('"') || text.Contains('\r') || text.Contains('\n'))
        //                    throw new Exception("Illegal character in string literal");
        //                sb.Append($"\"{text}\"");
        //                i += j + 2;
        //            }
        //            else if (b == 0x80)
        //            {
        //                sb.Append($"{BitConverter.ToSingle(bytes, i + 1)}");
        //                i += 4;
        //            }
        //            else if (b == 0x81)
        //            {
        //                sb.Append($"{BitConverter.ToDouble(bytes, i + 1)}");
        //                i += 8;
        //            }
        //            else if (b == 0x82)
        //            {
        //                sb.Append($"{BitConverter.ToInt32(bytes, i + 1)}");
        //                i += 4;
        //            }
        //            else if (b >= 0x84 && b <= 0x8A)
        //            {
        //                sb.Append($"({b - 0x84})");
        //            }
        //            else if (OperatorsByByte.ContainsKey(b))
        //            {
        //                sb.Append(OperatorsByByte[b]);
        //            }
        //            else if (b >= 0xA7 && b <= 0xAE)
        //            {
        //                sb.Append($">[{b - 0xA7}]");
        //            }
        //            else if (b >= 0xAF && b <= 0xB6)
        //            {
        //                sb.Append($"[{b - 0xAF}]>");
        //            }
        //            else if (b == 0xA1)
        //            {
        //                throw new Exception("Evaluators may not contain more than one 0xA1");
        //            }
        //            else
        //            {
        //                sb.Append($"#{b.ToString("X2")}");
        //            }
        //        }
        //    }

        //    return sb.ToString().TrimEnd();
        //}

        /// <summary>
        /// Dissembles bytecode into an  "EzLanguage" plain text expression.
        /// </summary>
        public static string DissembleExpression(byte[] bytes)
        {
            return EzInfixor.BytecodeToInfix(bytes);
        }
    }
}