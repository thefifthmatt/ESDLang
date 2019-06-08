using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormats;
using static ESDLang.EzSemble.AST;

namespace ESDLang.EzSemble
{
    public static partial class EzSembler
    {
        /// <summary>
        /// Dissembles a CommandCall object into a line of "EzLanguage" plain text.
        /// </summary>
        public static Statement DissembleCommandCall(EzSembleContext context, ESD.CommandCall c)
        {
            return new Statement { Name = context.GetCommandInfo(c.CommandBank, c.CommandID).Name, Args = c.Arguments.Select(a => DissembleExpression(context, a)).ToList() };
        }

        /// <summary>
        /// Dissembles a list of CommandCall objects into a plain text "EzLanguage" script.
        /// </summary>
        public static Block DissembleCommandScript(EzSembleContext context, List<ESD.CommandCall> script)
        {
            return new Block { Cmds = script.Select(x => DissembleCommandCall(context, x)).ToList() };
        }

        /// <summary>
        /// Dissembles bytecode into an "EzLanguage" expression.
        /// </summary>
        public static Expr DissembleExpression(EzSembleContext context, byte[] bytes)
        {
            return EzInfixor.BytecodeToInfix(context, bytes);
        }
    }
}
