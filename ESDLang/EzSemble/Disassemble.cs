using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormats;
using ESDLang.DLSE;
using static ESDLang.EzSemble.AST;
using ESDLang.Doc;

namespace ESDLang.EzSemble
{
    public static partial class EzSembler
    {
        public static Statement DissembleCommandCall(EzSembleContext context, ESD.CommandCall c)
        {
            if (EzSembleContext.UseNew)
            {
                context.Doc.Commands.TryGetValue((c.CommandBank, c.CommandID), out ESDDocumentation.MethodDoc method);
                List<Expr> args = c.Arguments.Select(a => DissembleExpression(context, a)).ToList();
                EzInfixor.AnnotateArgExprs(context, method, args);
                return new Statement { Name = method?.Name ?? $"{c.CommandBank}:{c.CommandID}", Bank = c.CommandBank, ID = c.CommandID, Args = args };
            }
            else
            {
                EzSembleContext.EzSembleMethodInfo method = context.GetCommandInfo(c.CommandBank, c.CommandID);
                List<Expr> args = c.Arguments.Select(a => DissembleExpression(context, a)).ToList();
                return new Statement { Name = method.Name, Bank = c.CommandBank, ID = c.CommandID, Args = args };
            }
        }

        public static Block DissembleCommandScript(EzSembleContext context, List<ESD.CommandCall> script)
        {
            return new Block { Cmds = script.Select(x => DissembleCommandCall(context, x)).ToList() };
        }

        public static Statement DissembleCommandCall(EzSembleContext context, ESDDLSE.Event c)
        {
            if (EzSembleContext.UseNew)
            {
                if (c is not ESDDLSE.ExternalEvent ev) throw new NotImplementedException($"ESD-DLSE command {c} not supported");
                string name = context.Doc.Commands.TryGetValue((1, ev.ID), out ESDDocumentation.MethodDoc method) ? method.Name : null;
                name ??= $"1:{ev.ID}";
                return new Statement { Name = name, Bank = 1, ID = ev.ID, Args = ev.Args.Select(a => DissembleExpression(context, a)).ToList() };
            }
            else
            {
                if (c is not ESDDLSE.ExternalEvent ev) throw new NotImplementedException($"ESD-DLSE command {c} not supported");
                return new Statement { Name = context.GetCommandInfo(1, ev.ID).Name, Bank = 1, ID = ev.ID, Args = ev.Args.Select(a => DissembleExpression(context, a)).ToList() };
            }
        }

        public static Block DissembleCommandScript(EzSembleContext context, List<ESDDLSE.Event> script)
        {
            return new Block { Cmds = script.Select(x => DissembleCommandCall(context, x)).ToList() };
        }

        public static Block DissembleCommandScript(EzSembleContext context, List<ESDDLSE.ExternalEvent> script)
        {
            return new Block { Cmds = script.Select(x => DissembleCommandCall(context, x)).ToList() };
        }

        public static Expr DissembleExpression(EzSembleContext context, byte[] bytes)
        {
            return EzInfixor.BytecodeToInfix(context, bytes);
        }
    }
}
