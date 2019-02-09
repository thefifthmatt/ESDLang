using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static SoulsFormats.ESD.ESD;

namespace SoulsFormats.ESD.EzSemble
{
    public class EzSembleContext
    {
        public Dictionary<(int Bank, int ID), string> CommandNamesByID;
        public Dictionary<string, (int Bank, int ID)> CommandIDsByName 
            => CommandNamesByID.ToDictionary(kvp => kvp.Value, kvp => kvp.Key);
        public Dictionary<int, string> FunctionNamesByID;
        public Dictionary<string, int> FunctionIDsByName
            => FunctionNamesByID.ToDictionary(kvp => kvp.Value, kvp => kvp.Key);

        internal class CompiledState
        {
            internal List<CommandCall> EntryCommands;
            internal List<CommandCall> ExitCommands;
            internal List<CommandCall> WhileCommands;
            internal CompiledState(EzSembleContext context, State s)
            {
                EntryCommands = EzSembler.AssembleCommandScript(context, s.EntryScript);
                ExitCommands = EzSembler.AssembleCommandScript(context, s.ExitScript);
                WhileCommands = EzSembler.AssembleCommandScript(context, s.WhileScript);
            }
        }

        internal class CompiledCondition
        {
            internal List<CommandCall> PassCommands;
            internal byte[] Evaluator;
            internal CompiledCondition(EzSembleContext context, Condition c)
            {
                PassCommands = EzSembler.AssembleCommandScript(context, c.PassScript);
                Evaluator = EzSembler.AssembleExpression(context, c.Evaluator);
            }
        }
        
        private Dictionary<State, CompiledState> CompiledStatesForSaving;
        private Dictionary<Condition, CompiledCondition> CompiledConditionsForSaving;

        internal CompiledState GetCompiledState(State s)
        {
            if (!CompiledStatesForSaving.ContainsKey(s))
            {
                CompiledStatesForSaving.Add(s, new CompiledState(this, s));
            }
            else if (s.NeedsCompile)
            {
                CompiledStatesForSaving[s] = new CompiledState(this, s);
                s.NeedsCompile = false;
            }

            return CompiledStatesForSaving[s];
        }

        internal CompiledCondition GetCompiledCondition(Condition c)
        {
            if (!CompiledConditionsForSaving.ContainsKey(c))
            {
                CompiledConditionsForSaving.Add(c, new CompiledCondition(this, c));
            }
            else if (c.NeedsCompile)
            {
                CompiledConditionsForSaving[c] = new CompiledCondition(this, c);
            }

            return CompiledConditionsForSaving[c];
        }

        public EzSembleContext()
        {
            CommandNamesByID = new Dictionary<(int Bank, int ID), string>();
            FunctionNamesByID = new Dictionary<int, string>();
            CompiledStatesForSaving = new Dictionary<State, CompiledState>();
            CompiledConditionsForSaving = new Dictionary<Condition, CompiledCondition>();
        }

        public string GetCommandName(int bank, int id)
        {
            if (CommandNamesByID.ContainsKey((bank, id)))
            {
                return CommandNamesByID[(bank, id)];
            }
            else
            {
                return $"{bank}:{id}";
            }
        }

        public (int Bank, int ID) GetCommandID(string name)
        {
            if (CommandIDsByName.ContainsKey(name))
            {
                return CommandIDsByName[name];
            }
            else
            {
                var regex = Regex.Match(name, @"(\d+):(\d+)");
                return (int.Parse(regex.Groups[1].Value), int.Parse(regex.Groups[2].Value));
            }
        }

        public string GetFunctionName(int id)
        {
            if (FunctionNamesByID.ContainsKey(id))
                return FunctionNamesByID[id];
            else
                return $"f{id}";
        }

        public int GetFunctionID(string name)
        {
            if (FunctionIDsByName.ContainsKey(name))
                return FunctionIDsByName[name];
            else
                return int.Parse(name.Substring(1));
        }
    }
}
