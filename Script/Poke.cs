using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SoulsFormats;
using ESDLang.Adapter;
using ESDLang.EzSemble;

namespace ESDLang.Script
{
    // Currently uses the adapted ESD format.
    // TODO: See if we can go back to SoulsFormat ESD.
    class Poke
    {
        private readonly string docPath;
        private readonly string dir;
        private readonly bool chr;
        private readonly string esdDir;
        public Poke(string[] args)
        {
            if (args.Contains("ds1"))
            {
                dir = @"C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS REMASTERED";
            }
            else if (args.Contains("ds3"))
            {
                dir = @"C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\Game";
            }
            else
            {
                dir = @"C:\Program Files (x86)\Steam\steamapps\common\Sekiro";
            }
            chr = args.Contains("chr");
            // For now, requires running from sln dir
            if (chr)
            {
                docPath = @"Script\ESDScriptingDocumentation_Chr.xml";
                esdDir = @"chr";
            }
            else
            {
                docPath = @"Script\ESDScriptingDocumentation_Talk.xml";
                esdDir = @"script\talk";
            }
        }

        private ESDL ReadESD(byte[] data, string path, int check=-1)
        {
            if (check > 1)
            {
                int esdId = int.Parse(path.Substring(1));
                if (esdId != check) return null;
            }
            EzSembleContext context = EzSembleContext.LoadFromXml(docPath);
            ESDL esd = new ESDL();
            esd.ReadWithContext(new BinaryReaderEx(false, data), context);
            return esd;
        }

        public void Custom(int esdId)
        {
            Dictionary<string, Dictionary<string, ESDL>> esds = LoadBnd(esdDir, (data, path) => ReadESD(data, path, esdId));
            if (esds.Count != 1) throw new Exception($"Found in {esds.Count} map");
            string map = esds.Keys.First();
            if (esds[map].Count != 1) throw new Exception($"Found in {esds[map].Count} esds within {map}");
            string name = esds[map].Keys.First();
            ESDL esd = esds[map][name];
            // Do custom logic here
        }

        public void Load()
        {
            LoadBnd(esdDir, (data, path) => ReadESD(data, path));
        }

        public void Save(bool write)
        {
            string outDir = @"testdata";
            Directory.CreateDirectory(outDir);
            ESDL CopyAndReadESD(byte[] data, string path)
            {
                string outPath = $@"{outDir}\{path}a.esd";
                if (write && !File.Exists(outPath)) File.WriteAllBytes(outPath, data);
                return ReadESD(data, path);
            }
            // Have ReadESD actually save bytes elsewhere
            Dictionary<string, Dictionary<string, ESDL>> esds = LoadBnd(esdDir, (data, path) => CopyAndReadESD(data, path));
            foreach (KeyValuePair<string, Dictionary<string, ESDL>> map in esds)
            {
                foreach (KeyValuePair<string, ESDL> esd in map.Value)
                {
                    byte[] data = WriteESD(esd.Value);
                    if (write) File.WriteAllBytes($@"{outDir}\{esd.Key}b.esd", data);
                }
            }
        }

        byte[] WriteESD(ESDL esd)
        {
            EzSembleContext context = EzSembleContext.LoadFromXml(docPath);
            // ESD esd = new ESD();
            using (MemoryStream stream = new MemoryStream())
            {
                esd.WriteWithContext(new BinaryWriterEx(false, stream), context);
                return stream.ToArray();
            }
        }

        public void Export()
        {
            Dictionary<string, Dictionary<string, ESDL>> esds = LoadBnd(esdDir, (data, path) => ReadESD(data, path));
            Directory.CreateDirectory($@"{dir}\yapped\script\talk");
            OverrideBnd(esdDir, @"yapped\script\talk", esds, esd => WriteESD(esd));
        }

        private Dictionary<string, Dictionary<string, T>> LoadBnd<T>(string relDir, Func<byte[], string, T> parser, string ext="*esdbnd.dcx")
        {
            Console.WriteLine($"{dir} - {relDir}");
            Dictionary<string, Dictionary<string, T>> ret = new Dictionary<string, Dictionary<string, T>>();
            foreach (string path in Directory.GetFiles($@"{dir}\{relDir}", ext))
            {
                string name = BaseName(path);
                Dictionary<string, T> bnds = new Dictionary<string, T>();
                IBinder bnd;
                try
                {
                    // :fatcat:
                    bnd = dir.IndexOf("REMASTERED") != -1 ? (IBinder)BND3.Read(path) : BND4.Read(path);
                }
                catch (Exception ex)
                {
                    throw new Exception($"Failed to load {path}: {ex}");
                }
                foreach (BinderFile file in bnd.Files)
                {
                    string bndName = BaseName(file.Name);
                    try
                    {
                        T res = parser(file.Bytes, bndName);
                        if (res != null) bnds[bndName] = res;
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Failed to load {path}: {bndName}: {ex}");
                    }
                }
                if (bnds.Count > 0)
                {
                    ret[name] = bnds;
                }
            }
            return ret;
        }
        private void OverrideBnd<T>(string fromDir, string toDir, Dictionary<string, Dictionary<string, T>> data, Func<T, byte[]> writer, string ext = "*bnd.dcx")
        {
            foreach (string path in Directory.GetFiles($@"{dir}\{fromDir}", ext))
            {
                string fname = Path.GetFileName(path);
                string name = BaseName(path);
                if (!data.ContainsKey(name)) continue;
                Dictionary<string, T> bnds = data[name];
                BND4 bnd;
                try
                {
                    bnd = BND4.Read(path);
                }
                catch (Exception ex)
                {
                    throw new Exception($"Failed to load {path}: {ex}");
                }
                foreach (BinderFile file in bnd.Files)
                {
                    string bndName = BaseName(file.Name);
                    if (!bnds.ContainsKey(bndName)) continue;
                    try
                    {
                        file.Bytes = writer(bnds[bndName]);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Failed to load {path}: {bndName}: {ex}");
                    }
                }
                string outPath = $@"{dir}\{toDir}\{fname}";
                Console.WriteLine($"Writing to {outPath}");
                bnd.Write(outPath, DCX.Type.DCX_KRAK);
            }
        }

        private string BaseName(string path)
        {
            path = Path.GetFileName(path);
            if (path.IndexOf('.') == -1) return path;
            return path.Substring(0, path.IndexOf('.'));
        }
    }
}
