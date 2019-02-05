using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace SoulsFormats.Formats.ESD
{
    /// <summary>
    /// Metadata for an ESD file.
    /// </summary>
    public class ESDMetadata
    {
        /// <summary>
        /// Metadata for an ESD State.
        /// </summary>
        public class StateMetadata
        {
            /// <summary>
            /// The name of an ESD State.
            /// </summary>
            public string Name;

            /// <summary>
            /// The script executed upon entering an ESD State.
            /// </summary>
            public string EntryScript;

            /// <summary>
            /// The script executed upon leaving an ESD State.
            /// </summary>
            public string ExitScript;

            /// <summary>
            /// The script executed at 30 Hz during an ESD State.
            /// </summary>
            public string WhileScript;

            /// <summary>
            /// Displays the ESD State metadata with its name when written as a string.
            /// </summary>
            public override string ToString() => $"StateMetadata: {Name}";
        }

        /// <summary>
        /// Metadata for an ESD Condition.
        /// </summary>
        public class ConditionMetadata
        {
            /// <summary>
            /// The name of an ESD Condition.
            /// </summary>
            public string Name;

            /// <summary>
            /// The boolean expression which an ESD Condition must evaluate.
            /// </summary>
            public string Evaluator;

            /// <summary>
            /// The script executed once an ESD Condition's Evaluator returns true.
            /// </summary>
            public string PassScript;

            /// <summary>
            /// Displays the ESD Condition metadata with its name when written as a string.
            /// </summary>
            public override string ToString() => $"ConditionMetadata: {Name}";
        }

        /// <summary>
        /// GUID of this metadata. Used to check that this metadata matches an ESD file.
        /// </summary>
        public string ESDHash;

        /// <summary>
        /// Names of the State Groups in an ESD file.
        /// </summary>
        public Dictionary<long, string> StateGroupNames;

        /// <summary>
        /// Metadata for the states in an ESD file.
        /// </summary>
        public Dictionary<long, Dictionary<long, StateMetadata>> StateMetadatas;

        /// <summary>
        /// Metadata for the conditions in an ESD file.
        /// </summary>
        public Dictionary<long, ConditionMetadata> ConditionMetadatas;

        internal const string INDENT = "  ";
        internal const string INDENT_STATE_SCRIPT = "          ";
        internal const string INDENT_CONDITION_SCRIPT = "      ";

        /// <summary>
        /// Creates a new blank ESD metadata object.
        /// </summary>
        public ESDMetadata()
        {
            ESDHash = System.Security.Cryptography.MD5.Create().ToString();
            StateGroupNames = new Dictionary<long, string>();
            StateMetadatas = new Dictionary<long, Dictionary<long, StateMetadata>>();
            ConditionMetadatas = new Dictionary<long, ConditionMetadata>();
        }

        private static string GetIndentedScript(string script, string elementTotalIndent)
        {
            string indentStr = elementTotalIndent.Substring(0, elementTotalIndent.Length - INDENT.Length);
            string joinStr = $"\n{indentStr}{INDENT}";
            return $"{joinStr}{(string.Join(joinStr, script.Split('\n')))}\n{indentStr}";
        }

        private static string GetUnindentedScript(string script, string elementTotalIndent)
        {
            string indentStr = elementTotalIndent.Substring(0, elementTotalIndent.Length - INDENT.Length);
            string joinStr = $"\n{indentStr}{INDENT}";
            return string.Join("\n", script.Split(new string[] { joinStr }, StringSplitOptions.None))
                .Replace("\r", "")
                .Trim(' ', '\n');
        }

        private void InnerWriteToXml(string xmlFileName)
        {
            XmlWriterSettings xws = new XmlWriterSettings();
            xws.Indent = true;
            xws.IndentChars = INDENT;
            XmlWriter xw = XmlWriter.Create(xmlFileName, xws);

            xw.WriteStartElement("EzStateMetadata");
            {
                xw.WriteAttributeString("Hash", ESDHash);
                xw.WriteStartElement("StateGroups");
                {
                    foreach (var g in StateMetadatas.Keys)
                    {
                        xw.WriteStartElement("StateGroup");
                        {
                            xw.WriteAttributeString("ID", g.ToString());
                            xw.WriteAttributeString("Name", StateGroupNames[g]);
                            xw.WriteStartElement("States");
                            {
                                foreach (var s in StateMetadatas[g])
                                {
                                    xw.WriteStartElement("State");
                                    {
                                        xw.WriteAttributeString("ID", s.Key.ToString());
                                        xw.WriteAttributeString("Name", s.Value.Name);

                                        xw.WriteStartElement("EntryScript");
                                        {
                                            xw.WriteString(GetIndentedScript(s.Value.EntryScript, INDENT_STATE_SCRIPT));
                                        }
                                        xw.WriteEndElement();

                                        xw.WriteStartElement("ExitScript");
                                        {
                                            xw.WriteString(GetIndentedScript(s.Value.ExitScript, INDENT_STATE_SCRIPT));
                                        }
                                        xw.WriteEndElement();

                                        xw.WriteStartElement("WhileScript");
                                        {
                                            xw.WriteString(GetIndentedScript(s.Value.WhileScript, INDENT_STATE_SCRIPT));
                                        }
                                        xw.WriteEndElement();

                                    }
                                    xw.WriteEndElement();
                                }
                            }
                            xw.WriteEndElement();
                        }
                        xw.WriteEndElement();
                    }
                }
                xw.WriteEndElement();

                xw.WriteStartElement("Conditions");
                {
                    foreach (var kvp in ConditionMetadatas)
                    {
                        xw.WriteStartElement("Condition");
                        {
                            xw.WriteAttributeString("ID", kvp.Key.ToString());
                            xw.WriteAttributeString("Name", kvp.Value.Name);

                            xw.WriteStartElement("Evaluator");
                            {
                                xw.WriteString(GetIndentedScript(kvp.Value.Evaluator, INDENT_CONDITION_SCRIPT));
                            }
                            xw.WriteEndElement();

                            xw.WriteStartElement("PassScript");
                            {
                                xw.WriteString(GetIndentedScript(kvp.Value.PassScript, INDENT_CONDITION_SCRIPT));
                            }
                            xw.WriteEndElement();
                        }
                        xw.WriteEndElement();
                    }
                }
                xw.WriteEndElement();
            }
            xw.WriteEndElement();
            xw.Close();
        }

        /// <summary>
        /// Writes metadata to an XML file.
        /// </summary>
        public void WriteToXml(string xmlFileName)
        {
            try
            {
                InnerWriteToXml(xmlFileName);
            }
            catch (Exception e)
            {
                throw new Exception($"Failed to write XML file \"{xmlFileName}\":\n{e.Message}", e);
            }
        }

        private static ESDMetadata InnerReadFromXml(string xmlFileName)
        {
            var meta = new ESDMetadata();

            XmlDocument xml = new XmlDocument();
            xml.Load(xmlFileName);

            meta.ESDHash = xml.SelectSingleNode("EzStateMetadata").Attributes["Hash"].InnerText;

            foreach (XmlNode groupNode in xml.SelectNodes("EzStateMetadata/StateGroups/StateGroup"))
            {
                long stateGroupID = long.Parse(groupNode.Attributes["ID"].InnerText);
                string stateGroupName = groupNode.Attributes["Name"].InnerText;
                meta.StateGroupNames.Add(stateGroupID, stateGroupName);
                meta.StateMetadatas.Add(stateGroupID, new Dictionary<long, StateMetadata>());
                foreach (XmlNode stateNode in groupNode.SelectNodes("States/State"))
                {
                    long stateID = long.Parse(stateNode.Attributes["ID"].InnerText);
                    string stateName = stateNode.Attributes["Name"].InnerText;
                    string stateEntryScript = GetUnindentedScript(stateNode.SelectSingleNode("EntryScript").InnerText, INDENT_STATE_SCRIPT);
                    string stateExitScript = GetUnindentedScript(stateNode.SelectSingleNode("ExitScript").InnerText, INDENT_STATE_SCRIPT);
                    string stateWhileScript = GetUnindentedScript(stateNode.SelectSingleNode("WhileScript").InnerText, INDENT_STATE_SCRIPT);
                    meta.StateMetadatas[stateGroupID].Add(stateID, new StateMetadata()
                    {
                        Name = stateName,
                        EntryScript = stateEntryScript,
                        ExitScript = stateExitScript,
                        WhileScript = stateWhileScript,
                    });
                }
            }

            foreach (XmlNode conditionNode in xml.SelectNodes("EzStateMetadata/Conditions/Condition"))
            {
                long conditionID = long.Parse(conditionNode.Attributes["ID"].InnerText);
                string conditionName = conditionNode.Attributes["Name"].InnerText;
                string conditionEvaluator = GetUnindentedScript(conditionNode.SelectSingleNode("Evaluator").InnerText, INDENT_CONDITION_SCRIPT);
                string conditionPassScript = GetUnindentedScript(conditionNode.SelectSingleNode("PassScript").InnerText, INDENT_CONDITION_SCRIPT);
                meta.ConditionMetadatas.Add(conditionID, new ConditionMetadata()
                {
                    Name = conditionName,
                    Evaluator = conditionEvaluator,
                    PassScript = conditionPassScript,
                });
            }

            return meta;
        }

        /// <summary>
        /// Reads metadata from an XML file.
        /// </summary>
        public static ESDMetadata ReadFromXml(string xmlFileName)
        {
            try
            {
                return InnerReadFromXml(xmlFileName);
            }
            catch (Exception e)
            {
                throw new Exception($"Failed to read XML file \"{xmlFileName}\":\n{e.Message}", e);
            }
        }

        /// <summary>
        /// Generates metadata based on the in-memory ESD file.
        /// </summary>
        public static ESDMetadata Generate(SoulsFormats.ESD.ESD esd)
        {
            var meta = new ESDMetadata();

            meta.ESDHash = esd.LastSavedHash;

            meta.StateGroupNames = esd.StateGroupNames;

            foreach (var g in esd.StateGroups.Keys)
            {
                meta.StateMetadatas.Add(g, new Dictionary<long, StateMetadata>());
                foreach (var s in esd.StateGroups[g].Keys)
                {
                    meta.StateMetadatas[g].Add(s, new StateMetadata()
                    {
                        Name = esd.StateGroups[g][s].Name,
                        EntryScript = esd.StateGroups[g][s].EntryScript,
                        ExitScript = esd.StateGroups[g][s].ExitScript,
                        WhileScript = esd.StateGroups[g][s].WhileScript,
                    });
                }
            }

            foreach (var g in esd.GetAllConditions())
            {
                foreach (var c in g.Value)
                {
                    meta.ConditionMetadatas.Add(c.MetaRefID, new ConditionMetadata()
                    {
                        Name = c.Name,
                        Evaluator = c.Evaluator,
                        PassScript = c.PassScript,
                    });
                }
            }

            return meta;
        }

        /// <summary>
        /// Applies metadata to an in-memory ESD, adding additional info.
        /// </summary>
        public static void Apply(SoulsFormats.ESD.ESD esd, ESDMetadata meta)
        {
            if (meta.ESDHash.Trim().ToUpper() != esd.LastSavedHash.Trim().ToUpper())
            {
                throw new Exception("MD5 Hash of ESD file does not match that of the saved metadata. Metadata was not made for this ESD file.");
            }

            esd.StateGroupNames = meta.StateGroupNames;

            foreach (var g in esd.StateGroups.Keys)
            {
                foreach (var s in esd.StateGroups[g].Keys)
                {
                    esd.StateGroups[g][s].Name = meta.StateMetadatas[g][s].Name;
                    esd.StateGroups[g][s].EntryScript = meta.StateMetadatas[g][s].EntryScript;
                    esd.StateGroups[g][s].ExitScript = meta.StateMetadatas[g][s].ExitScript;
                    esd.StateGroups[g][s].WhileScript = meta.StateMetadatas[g][s].WhileScript;
                }
            }

            foreach (var g in esd.GetAllConditions())
            {
                foreach (var c in g.Value)
                {
                    c.Name = meta.ConditionMetadatas[c.MetaRefID].Name;
                    c.Evaluator = meta.ConditionMetadatas[c.MetaRefID].Evaluator;
                    c.PassScript = meta.ConditionMetadatas[c.MetaRefID].PassScript;
                }
            }
        }
    }
}
