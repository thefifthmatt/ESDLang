using System;
using System.IO;
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
            if (args.Length == 0)
            {
                Console.WriteLine(ESDOptions.GetShortUsage());
            }
            else if (args.Contains("-h") || args.Contains("-H"))
            {
                Console.WriteLine(ESDOptions.GetUsage());
            }
            else
            {
                ESDOptions options;
                try
                {
                    options = ESDOptions.Parse(args);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"ERROR: {e.Message}");
                    Console.WriteLine(); 
                    Console.WriteLine(ESDOptions.GetShortUsage());
                    return;
                }
                while (true)
                {
                    ESDOptions.Option opt;
                    try
                    {
                        opt = options.NextAction();
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine($"Error processing command: {e.Message}");
                        return;
                    }
                    if (opt == null) break;
                    new CommandRunner(options, opt).Run();
                }
            }
        }
    }
}
