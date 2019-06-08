using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ESDLang.Script
{
    class Program
    {
        static void Main(string[] args)
        {
            bool usage = false;
            if (args.Length > 0)
            {
                Poke p = new Poke(args);
                if (int.TryParse(args[0], out int esdId)) p.Custom(esdId);
                else if (args[0].Equals("load")) p.Load();
                else if (args[0].Equals("save")) p.Save(true);
                else if (args[0].Equals("testsave")) p.Save(false);
                else if (args[0].Equals("export")) p.Export();
                else usage = true;
            }
            else
            {
                usage = true;
            }
            if (usage)
            {
                Console.WriteLine("Experimental mode. Usage:");
                Console.WriteLine("  esdtool.exe <number> : Run custom routine for a given esd");
                Console.WriteLine("  esdtool.exe load     : Load all esds and exit");
                Console.WriteLine("  esdtool.exe testave  : Load and reparse all esds and exit");
                Console.WriteLine("  esdtool.exe save     : Load all esds and write unpacked original + reparsed to testdata/");
                Console.WriteLine("  esdtool.exe export   : Load all esds and export to yapped/ subdir of game dir");
                Console.WriteLine("  Other options: ds1/ds3 - use that game dir. chr - use DS1 chr bnds.");
            }
        }
    }
}
