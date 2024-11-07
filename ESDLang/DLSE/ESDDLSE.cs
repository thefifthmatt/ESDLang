using SoulsFormats;
using System;
using System.Collections.Generic;
using System.IO;

namespace ESDLang.DLSE
{
    public class ESDDLSE : SoulsFile<ESDDLSE>
    {
        private int Version { get; set; }

        public int Unk08 { get; set; }

        // public List<object> UnkReferences { get; set; }
        // TODO: How does this work across multiple mapstates?
        // This is maintained for v3, but Transition.State works for both v1 and v3
        private Dictionary<Transition, MapState> Transitions { get; set; }

        // TODO may need to fill this in
        public int Unk10 { get; set; }

        private List<string> SharedStrings { get; set; }

        public List<Map> Maps { get; set; }

        public long UnkID { get; set; }

        public override string ToString() => $"ESD[{Unk08}, {Unk10}, {Maps.Count} Maps, {UnkID:X}]";

        protected override void Read(BinaryReaderEx br)
        {
            br.BigEndian = true;

            // Header
            br.AssertASCII("DLSE");
            br.AssertInt16(2);
            // Version
            Version = br.ReadInt16();
            if (Version != 1 && Version != 3) throw new NotImplementedException($"Only ESD-DLSE versions 1 and 3 are supported, got version {Version}");
            int refCount = -1;
            if (Version == 3)
            {
                Unk08 = br.ReadInt32();
                refCount = br.ReadInt32();
                Unk10 = br.ReadInt32();
            }
            short stringCount = br.ReadInt16();
            SharedStrings = new List<string>(stringCount);
            for (int i = 0; i < stringCount; i++)
            {
                int length = br.ReadInt32();
                string str = br.ReadASCII(length);
                SharedStrings.Add(str);
            }

            ReadState state = new ReadState { SharedStrings = SharedStrings };
            if (Version == 3)
            {
                state.Refs = new List<object>();
            }
            else
            {
                state.RefMap = new Dictionary<int, object>();
            }

            // Project
            AssertTypeName(br, state, "EzStateProject");
            br.AssertInt32(2);
            Maps = ReadDLVector(br, state, Map.Read);
            UnkID = br.ReadInt64();
            if (Version == 3)
            {
                // These should all be references
                List<MapState> targets = new List<MapState>(refCount);
                for (int i = 0; i < refCount; i++)
                {
                    string type = GetTypeName(br, state);
                    // qConsole.WriteLine(type);
                    object obj;
                    switch (type)
                    {
                        case MapState.TypeName:
                            obj = MapState.Read(br, state);
                            break;
                        case Transition.TypeName:
                            obj = Transition.Read(br, state);
                            break;
                        default:
                            throw new InvalidDataException($"Read {type} | Expected transition or state type");
                    }
                    if (obj is not MapState target) throw new NotImplementedException("Nested transition references are not yet understood/supported");
                    // Console.WriteLine($"{i}: {obj}");
                    targets.Add(target);
                }
                Transitions = new();
                int targetIndex = 0;
                foreach (Map map in Maps)
                {
                    foreach (Transition trans in map.Transitions)
                    {
                        MapState mapState = targets[targetIndex++];
                        Transitions[trans] = mapState;
                        trans.State = mapState;
                    }
                }
                if (targetIndex != targets.Count) throw new InvalidDataException($"Insufficient {targetIndex} transitions given {targets.Count} listed states");
            }
            else
            {
                // Could set Transitions dictionary here, but keep it internal for now
            }
        }

        // private string GetTypeName(int type) => SharedStrings[type - 1];
        private static string GetTypeName(BinaryReaderEx br, ReadState state)
        {
            short type = br.GetInt16(br.Position);
            return state.SharedStrings[type - 1];
        }

        private static void AssertTypeName(BinaryReaderEx br, ReadState state, string name)
        {
            short type = br.ReadInt16();
            string typeName = state.SharedStrings[type - 1];
            if (typeName != name) throw new InvalidDataException($"Read {typeName} (type {type}) at {br.Position - 2:X} | Expect {name}");
        }

        internal struct ReadState
        {
            // In v3, all refs appear in file order
            public List<object> Refs { get; set; }
            // In v1, it's just memory addresses
            public Dictionary<int, object> RefMap { get; set; }
            public List<string> SharedStrings { get; set; }
        }

        private static List<T> ReadDLVector<T>(BinaryReaderEx br, ReadState state, Func<BinaryReaderEx, ReadState, T> readRef)
        {
            AssertTypeName(br, state, "DLVector");
            int count = br.ReadInt32();
            // Console.WriteLine($"{count} {typeof(T)} at {br.Position - 6:X}");
            List<T> vals = new List<T>(count);
            for (int i = 0; i < count; i++)
            {
                vals.Add(readRef(br, state));
            }
            return vals;
        }

        private static bool ReadRef<T>(BinaryReaderEx br, ReadState state, string type, out T val) where T : class, new()
        {
            AssertTypeName(br, state, type);
            int id = br.ReadInt32();
            if (id == 0)
            {
                val = null;
                return true;
            }
            if (state.Refs != null)
            {
                // Console.WriteLine($"> Ref {typeof(T)} {id} at {br.Position - 6:X} - {(id > state.Refs.Count ? "new" : "existing")}");
                if (id > state.Refs.Count)
                {
                    // This is apparently not always the case, but figure it out when it comes up
                    if (id != state.Refs.Count + 1) throw new InvalidDataException($"Read ref ID {id} for {type} | Expect {state.Refs.Count + 1}");
                    val = new();
                    state.Refs.Add(val);
                    return false;
                }
                else
                {
                    val = state.Refs[id - 1] as T;
                    if (val == null) throw new InvalidDataException($"Read ref type {state.Refs[id - 1]} (id {id}) | Expect {type}");
                    return true;
                }
            }
            else
            {
                // Console.WriteLine($"> Ref {typeof(T)} {id} at {br.Position - 6:X} - {(state.RefMap.ContainsKey(id) ? "new" : "existing")}");
                if (state.RefMap.TryGetValue(id, out object value))
                {
                    val = value as T;
                    if (val == null) throw new InvalidDataException($"Read ref type {state.Refs[id - 1]} (id {id}) | Expect {type}");
                    return true;
                }
                else
                {
                    val = new();
                    state.RefMap[id] = val;
                    return false;
                }
            }
        }

        private static byte[] ReadBuffer(BinaryReaderEx br, ReadState state)
        {
            AssertTypeName(br, state, "buffer");
            int length = br.ReadInt32();
            return br.ReadBytes(length);
        }

        private static byte[] ReadEvaluator(BinaryReaderEx br, ReadState state)
        {
            // Just nest it all up. None of these deserve classes
            AssertTypeName(br, state, "EzStateEvaluator");
            br.AssertInt32(1);
            AssertTypeName(br, state, "DLVector");
            int length = br.ReadInt32();
            return br.ReadBytes(length);
        }

        public class Map
        {
            // TODO: This should be determined by overall version if it's all consistent
            private int Version { get; set; }
            public int ID { get; set; }
            public MapState StartState { get; set; }
            public List<MapState> States { get; set; }
            public List<Transition> Transitions { get; set; }

            internal const string TypeName = "EzStateMap";

            internal static Map Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out Map val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                val.Version = br.AssertInt32(1, 2);
                val.ID = br.ReadInt32();
                val.StartState = MapState.Read(br, state);
                val.States = ReadDLVector(br, state, MapState.Read);
                // These seem to be all references. Corresponds to v3 overall
                if (val.Version == 2)
                {
                    val.Transitions = ReadDLVector(br, state, Transition.Read);
                }
                return val;
            }

            public override string ToString() => $"Map[ID={ID}{(StartState == null ? "" : ", StartState")}, {States.Count} States, {Transitions.Count} Transitions]";
        }

        public class MapState
        {
            // TODO: This should be determined by overall version if it's all consistent
            private int Version { get; set; }
            public int ID { get; set; }
            public List<Transition> Transitions { get; set; }
            public List<ExternalEvent> EntryEvents { get; set; }
            public List<ExternalEvent> ExitEvents { get; set; }

            internal const string TypeName = "EzStateMapState";

            internal static MapState Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out MapState val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                val.Version = br.AssertInt32(1, 2);
                val.ID = br.ReadInt32();
                val.Transitions = ReadDLVector(br, state, Transition.Read);
                val.EntryEvents = ReadDLVector(br, state, ExternalEvent.Read);
                val.ExitEvents = ReadDLVector(br, state, ExternalEvent.Read);
                return val;
            }

            public override string ToString() => $"MapState[ID={ID}, {Transitions.Count} Transitions, {EntryEvents.Count} A, {ExitEvents.Count} B]";
        }

        public class Transition
        {
            // TODO: This should be determined by overall version if it's all consistent
            private int Version { get; set; }
            public byte[] Evaluator { get; set; }
            public List<Event> PassEvents { get; set; }
            // Only part of the format in v1, but it's set in both
            public MapState State { get; set; }

            internal const string TypeName = "EzStateTransition";

            internal static Transition Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out Transition val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                val.Version = br.AssertInt32(1, 3);
                if (val.Version == 1)
                {
                    CondEvaluator cond = CondEvaluator.Read(br, state);
                    val.Evaluator = cond.Data;
                    val.State = MapState.Read(br, state);
                    val.PassEvents = ReadDLVector(br, state, Event.ReadEvent);
                }
                else
                {
                    val.Evaluator = ReadBuffer(br, state);
                    val.PassEvents = ReadDLVector(br, state, Event.ReadEvent);
                }
                return val;
            }

            public override string ToString() => $"Transition[Condition=byte[{Evaluator.Length}], {PassEvents.Count} Events]";
        }

        // Only used in v1. Keep it internal for now for API consistency; write will either need to support them or transform them.
        private class CondEvaluator
        {
            // public Evaluator Evaluator { get; set; }
            public byte[] Data { get; set; }

            internal const string TypeName = "EzState::detail::EzStateCondition";

            internal static CondEvaluator Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out CondEvaluator val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                br.AssertInt32(1);
                val.Data = ReadEvaluator(br, state);
                return val;
            }
        }

        private class Evaluator
        {
            public byte[] Data { get; set; }

            internal const string TypeName = "EzStateEvaluator";

            internal static Evaluator Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out Evaluator val))
                {
                    return val;
                }
                br.AssertInt32(1);
                val.Data = ReadBuffer(br, state);
                return val;
            }
        }

        public abstract class Event
        {
            internal static Event ReadEvent(BinaryReaderEx br, ReadState state)
            {
                string type = GetTypeName(br, state);
                switch (type)
                {
                    case TransitionHostEvent.TypeName:
                        return TransitionHostEvent.Read(br, state);
                    case ExternalEvent.TypeName:
                        return ExternalEvent.Read(br, state);
                    default:
                        throw new InvalidDataException($"Read {type} | Expected event type");
                }
            }
        }

        public class TransitionHostEvent : Event
        {
            internal const string TypeName = "EzStateTransitionHostEvent";

            internal static TransitionHostEvent Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out TransitionHostEvent val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                br.AssertInt32(1);
                return val;
            }

            public override string ToString() => $"TransitionHostEvent[]";
        }

        public class ExternalEvent : Event
        {
            private int Version { get; set; }
            public int ID { get; set; }
            public List<byte[]> Args { get; set; }

            internal const string TypeName = "EzStateExternalEventT<ES_EVENT_PARAM_NUM_6>";

            internal static ExternalEvent Read(BinaryReaderEx br, ReadState state)
            {
                if (ReadRef(br, state, TypeName, out ExternalEvent val))
                {
                    return val;
                }
                AssertTypeName(br, state, TypeName);
                val.Version = br.AssertInt32(1, 2);
                val.ID = br.ReadInt32();
                int count = br.ReadInt32();
                val.Args = new List<byte[]>(count);
                for (int i = 1; i < count; i++)
                {
                    if (val.Version == 1)
                    {
                        val.Args.Add(ReadEvaluator(br, state));
                    }
                    else
                    {
                        val.Args.Add(ReadBuffer(br, state));
                    }
                }
                return val;
            }

            public override string ToString() => $"ExternalEvent[ID={ID}, {Args.Count} Args]";
        }
    }
}
