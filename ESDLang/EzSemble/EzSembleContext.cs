using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Xml;
using static ESDLang.Adapter.ESDL;

namespace ESDLang.EzSemble
{
    public class EzSembleContext
    {
        public class EzSembleMethodArgInfo
        {
            public string Name;
            public string ValueType = "Number";
            public string Description = "";
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
            public string Name;
            public string Description = "";
            public List<EzSembleMethodArgInfo> Args = new List<EzSembleMethodArgInfo>();
            public EzSembleMethodInfo()
            {

            }
            public EzSembleMethodInfo(string name)
            {
                Name = name;
            }
        }

        internal bool IsBigEndian = false;

        internal Dictionary<(int Bank, int ID), EzSembleMethodInfo> CommandInfoByID;
        internal Dictionary<string, (int Bank, int ID)> CommandIDsByName 
            => CommandInfoByID.ToDictionary(kvp => kvp.Value.Name, kvp => kvp.Key);
        internal Dictionary<int, EzSembleMethodInfo> FunctionInfoByID;
        internal Dictionary<string, int> FunctionIDsByName
            => FunctionInfoByID.ToDictionary(kvp => kvp.Value.Name, kvp => kvp.Key);
        internal Dictionary<string, List<EzSembleEnumEntry>> EnumInfo;

        public EzSembleContext()
        {
            CommandInfoByID = new Dictionary<(int Bank, int ID), EzSembleMethodInfo>();
            FunctionInfoByID = new Dictionary<int, EzSembleMethodInfo>();
            EnumInfo = new Dictionary<string, List<EzSembleEnumEntry>>();
        }

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

                    newCommandInfo.Args.Add(newArgInfo);
                }

                context.CommandInfoByID.Add((bankID, commandID), newCommandInfo);
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

            return context;
        }

        public void WriteToXml(string xmlFileName)
        {
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
