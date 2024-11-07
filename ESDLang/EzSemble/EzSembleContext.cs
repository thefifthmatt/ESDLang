using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Xml;
using ESDLang.Doc;

namespace ESDLang.EzSemble
{
    public class EzSembleContext
    {
        // Pointers to new config
        // Eventually this file and much of the EzSemble namespace could be removed or split out.
        public static bool UseNew { get; set; } = true;
        public ESDDocumentation Doc { get; set; }

        public class EzSembleMethodArgInfo
        {
            public string Name;
            public string ValueType;
            public string Description = "";
            public string EnumName;
            public string Namespace;
            public bool Optional;

            public EzSembleMethodArgInfo()
            {

            }
            public EzSembleMethodArgInfo(string name)
            {
                Name = name;
            }
            public EzSembleMethodArgInfo(string name, string valueType, string desc)
            {
                Name = name;
                ValueType = valueType;
                Description = desc;
            }
            public EzSembleMethodArgInfo Clone()
            {
                return (EzSembleMethodArgInfo)MemberwiseClone();
            }

            public override string ToString() => $"Arg[{Name}:Type={ValueType}{(Description == null ? "" : ",Comment=")}{Description}]";
        }

        public class EzSembleEnumEntry
        {
            public string Value;
            public string Name;
            public string Description = "";
            public EzSembleEnumEntry()
            {

            }
            public EzSembleEnumEntry(string name)
            {
                Name = name;
            }
        }

        public class EzSembleMethodInfo
        {
            // TODO: Previous names
            public string Name;
            public string Description = "";
            public List<EzSembleMethodArgInfo> Args = new List<EzSembleMethodArgInfo>();
            public EzSembleMethodArgInfo ReturnValue;

            public EzSembleMethodInfo()
            {

            }
            public EzSembleMethodInfo(string name)
            {
                Name = name;
            }
            public EzSembleMethodInfo Clone()
            {
                EzSembleMethodInfo other = (EzSembleMethodInfo)MemberwiseClone();
                if (other.Args != null) other.Args = other.Args.Select(a => a.Clone()).ToList();
                return other;
            }

            public override string ToString() => $"Method[{Name}{(ReturnValue == null ? "" : $"->{ReturnValue}")}{(Args.Count > 0 ? ": " : "")}{string.Join(", ", Args)}]";
        }

        internal bool IsBigEndian = false;

        // Temporarily public for migration
        public readonly Dictionary<(int Bank, int ID), EzSembleMethodInfo> CommandInfoByID;
        public readonly Dictionary<int, EzSembleMethodInfo> FunctionInfoByID;
        public readonly Dictionary<string, List<EzSembleEnumEntry>> EnumInfo;

        internal Dictionary<string, (int Bank, int ID)> CommandIDsByName;
        internal Dictionary<string, int> FunctionIDsByName;

        public EzSembleContext()
        {
            CommandInfoByID = new Dictionary<(int Bank, int ID), EzSembleMethodInfo>();
            CommandIDsByName = new Dictionary<string, (int Bank, int ID)>();
            FunctionInfoByID = new Dictionary<int, EzSembleMethodInfo>();
            FunctionIDsByName = new Dictionary<string, int>();
            EnumInfo = new Dictionary<string, List<EzSembleEnumEntry>>();
        }

        // Temporarily made private to migrate
        public IEnumerable<EzSembleMethodInfo> GetAllMethods() => CommandInfoByID.Values.Concat(FunctionInfoByID.Values);

        public EzSembleMethodInfo GetCommandInfo(int bank, int id)
        {
            if (CommandInfoByID.ContainsKey((bank, id)))
            {
                return CommandInfoByID[(bank, id)];
            }
            else
            {
                return new EzSembleMethodInfo($"{bank}:{id}");
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
                var regex = Regex.Match(name, @"(\d+):(-?\d+)");
                if (regex.Groups.Count == 3 
                    && int.TryParse(regex.Groups[1].Value, out int cmdBank) 
                    && int.TryParse(regex.Groups[2].Value, out int cmdID))
                {
                    return (cmdBank, cmdID);
                }
                else
                {
                    throw new Exception($"Command name '{name}' does not exist in the loaded XML documentation and" +
                        $" couldn't be parsed as a <Bank>:<ID>() representation of the command.");
                }
            }
        }

        public EzSembleMethodInfo GetFunctionInfo(int id)
        {
            if (FunctionInfoByID.ContainsKey(id))
            {
                return FunctionInfoByID[id];
            }
            else
            {
                return new EzSembleMethodInfo($"f{id}");
            }
        }

        public int GetFunctionID(string name)
        {
            if (FunctionIDsByName.ContainsKey(name))
            {
                return FunctionIDsByName[name];
            }
            else
            {
                if (name.ToUpper().StartsWith("F") && int.TryParse(name.Substring(1), out int funcID))
                {
                    return funcID;
                }
                else
                {
                    throw new Exception($"Function name '{name}' does not exist in the loaded XML documentation and" +
                        $" couldn't be parsed as a f<ID>() representation of the function.");
                }
            }
        }

        public List<string> GetAllEnumNames()
        {
            return EnumInfo.Keys.ToList();
        }

        public List<string> GetAllFunctionNames()
        {
            return FunctionIDsByName.Keys.ToList();
        }

        public List<string> GetAllCommandNames()
        {
            return CommandIDsByName.Keys.ToList();
        }

        public List<EzSembleEnumEntry> GetEnumEntries(string enumName)
        {
            return EnumInfo[enumName];
        }

        public bool TryGetEnumEntries(string enumName, out List<EzSembleEnumEntry> entries)
        {
            return EnumInfo.TryGetValue(enumName, out entries);
        }

        public static EzSembleContext LoadFromXml(string xmlFileName)
        {
            var context = new EzSembleContext();

            XmlDocument xml = new XmlDocument();
            xml.Load(xmlFileName);

            foreach (XmlNode commandNode in xml.SelectNodes("EzSembleContext/CommandList/Command"))
            {
                var newCommandInfo = new EzSembleMethodInfo();

                int bankID = int.Parse(commandNode.Attributes["Bank"].InnerText);
                int commandID = int.Parse(commandNode.Attributes["ID"].InnerText);

                newCommandInfo.Name = commandNode.Attributes["Name"].InnerText;
                newCommandInfo.Description = commandNode.Attributes["Description"].InnerText;

                foreach (XmlNode argNode in commandNode.SelectNodes("Arg"))
                {
                    var newArgInfo = new EzSembleMethodArgInfo();

                    newArgInfo.Name = argNode.Attributes["Name"].InnerText;
                    newArgInfo.ValueType = argNode.Attributes["ValueType"].InnerText;
                    newArgInfo.Description = argNode.Attributes["Description"].InnerText;
                    newArgInfo.Namespace = argNode.Attributes["Namespace"]?.InnerText;

                    newCommandInfo.Args.Add(newArgInfo);
                }

                context.CommandInfoByID.Add((bankID, commandID), newCommandInfo);

                // This could be made an optional feature, but every game after DS1 appears to support conditional bank ids
                if (bankID == 1)
                {
                    EzSembleMethodInfo ifInfo = newCommandInfo.Clone();
                    ifInfo.Name = newCommandInfo.Name + "If";
                    // Same as regular command, except the first arg is a boolean.
                    if (ifInfo.Args != null)
                    {
                        ifInfo.Args.Insert(0, new EzSembleMethodArgInfo
                        {
                            Name = "ExecIf",
                            ValueType = "Bool",
                        });
                    }
                    context.CommandInfoByID.Add((5, commandID), ifInfo);
                }
            }

            foreach (XmlNode functionNode in xml.SelectNodes("EzSembleContext/FunctionList/Function"))
            {
                var newFunctionInfo = new EzSembleMethodInfo();

                int functionID = int.Parse(functionNode.Attributes["ID"].InnerText);

                newFunctionInfo.Name = functionNode.Attributes["Name"].InnerText;
                newFunctionInfo.Description = functionNode.Attributes["Description"].InnerText;

                foreach (XmlNode argNode in functionNode.SelectNodes("Arg"))
                {
                    var newArgInfo = new EzSembleMethodArgInfo();

                    newArgInfo.Name = argNode.Attributes["Name"].InnerText;
                    newArgInfo.ValueType = argNode.Attributes["ValueType"].InnerText;
                    newArgInfo.Description = argNode.Attributes["Description"].InnerText;
                    newArgInfo.Namespace = argNode.Attributes["Namespace"]?.InnerText;

                    newFunctionInfo.Args.Add(newArgInfo);
                }

                context.FunctionInfoByID.Add(functionID, newFunctionInfo);
            }

            foreach (XmlNode enumNode in xml.SelectNodes("EzSembleContext/EnumList/Enum"))
            {
                string enumName = enumNode.Attributes["Name"].InnerText;
                List<EzSembleEnumEntry> enumEntries = new List<EzSembleEnumEntry>();
                foreach (XmlNode enumEntryNode in enumNode.SelectNodes("EnumEntry"))
                {
                    var newEnumEntry = new EzSembleEnumEntry();

                    newEnumEntry.Value = enumEntryNode.Attributes["Value"].InnerText;
                    newEnumEntry.Name = enumEntryNode.Attributes["Name"].InnerText;
                    newEnumEntry.Description = enumEntryNode.Attributes["Description"].InnerText;

                    enumEntries.Add(newEnumEntry);
                }

                context.EnumInfo.Add(enumName, enumEntries);
            }

            context.CommandIDsByName = context.CommandInfoByID.ToDictionary(kvp => kvp.Value.Name, kvp => kvp.Key);
            context.FunctionIDsByName = context.FunctionInfoByID.ToDictionary(kvp => kvp.Value.Name, kvp => kvp.Key);


            return context;
        }

        public void WriteToXml(string xmlFileName)
        {
            // TODO: Update with all attributes
            XmlWriterSettings xws = new XmlWriterSettings();
            xws.Encoding = Encoding.Unicode;
            xws.Indent = true;
            xws.IndentChars = "    ";
            XmlWriter xw = XmlWriter.Create(xmlFileName, xws);

            xw.WriteStartElement("EzSembleContext");
            {
                xw.WriteStartElement("CommandList");
                {
                    foreach (var kvp in CommandInfoByID)
                    {
                        if (kvp.Key.Bank == 5)
                        {
                            continue;
                        }
                        xw.WriteStartElement("Command");
                        {
                            xw.WriteAttributeString("Bank", kvp.Key.Bank.ToString());
                            xw.WriteAttributeString("ID", kvp.Key.ID.ToString());
                            xw.WriteAttributeString("Name", kvp.Value.Name);
                            xw.WriteAttributeString("Description", kvp.Value.Description);

                            foreach (var arg in kvp.Value.Args)
                            {
                                xw.WriteStartElement("Arg");
                                {
                                    xw.WriteAttributeString("Name", arg.Name);
                                    xw.WriteAttributeString("ValueType", arg.ValueType);
                                    xw.WriteAttributeString("Description", arg.Description);
                                }
                                xw.WriteEndElement();
                            }
                        }
                        xw.WriteEndElement();
                    }
                }
                xw.WriteEndElement();

                xw.WriteStartElement("FunctionList");
                {
                    foreach (var kvp in FunctionInfoByID)
                    {
                        xw.WriteStartElement("Function");
                        {
                            xw.WriteAttributeString("ID", kvp.Key.ToString());
                            xw.WriteAttributeString("Name", kvp.Value.Name);
                            xw.WriteAttributeString("Description", kvp.Value.Description);

                            foreach (var arg in kvp.Value.Args)
                            {
                                xw.WriteStartElement("Arg");
                                {
                                    xw.WriteAttributeString("Name", arg.Name);
                                    xw.WriteAttributeString("ValueType", arg.ValueType);
                                    xw.WriteAttributeString("Description", arg.Description);
                                }
                                xw.WriteEndElement();
                            }
                        }
                        xw.WriteEndElement();
                    }
                }
                xw.WriteEndElement();

                xw.WriteStartElement("EnumList");
                {
                    foreach (var kvp in EnumInfo)
                    {
                        xw.WriteStartElement("Enum");
                        {
                            xw.WriteAttributeString("Name", kvp.Key);

                            foreach (var enumEntry in kvp.Value)
                            {
                                xw.WriteStartElement("EnumEntry");
                                {
                                    xw.WriteAttributeString("Value", enumEntry.Value);
                                    xw.WriteAttributeString("Name", enumEntry.Name);
                                    xw.WriteAttributeString("Description", enumEntry.Description);
                                }
                                xw.WriteEndElement();
                            }
                        }
                        xw.WriteEndElement();
                    }
                }
                xw.WriteEndElement();

            }
            xw.WriteEndElement();
            xw.Close();
        }
    }
}
