using System;
using System.IO;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace ESDLang.Script
{
    class Program
    {
        [DllImport("kernel32")]
        static extern bool AllocConsole();

        [DllImport("kernel32")]
        static extern bool FreeConsole();

        static void Main(string[] args)
        {
            Thread.CurrentThread.CurrentCulture = CultureInfo.InvariantCulture;
            Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
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
                if (args.Length > 0 && args.All(a => File.Exists(a) || Directory.Exists(a)))
                {
                    // Assume drag and drop mode
                    Directory.SetCurrentDirectory(Path.GetDirectoryName(System.Reflection.Assembly.GetEntryAssembly().Location));
                    AllocConsole();
                    try
                    {
                        Console.WriteLine();
                        OptionsConfig config = null;
                        try
                        {
                            config = OptionsConfig.GetOrCreate(args[0]);
                        }
                        catch (Exception e)
                        {
                            Console.WriteLine(e);
                        }
                        Console.WriteLine("------------------------");
                        Console.WriteLine();
                        if (config != null)
                        {
                            List<string> configArgs = config.MakeOptions(args);
                            if (configArgs != null)
                            {
                                Console.WriteLine($"esdtool.exe {string.Join(" ", configArgs.Select(t => t.Contains(' ') ? $"\"{t}\"" : t))}");
                                Console.WriteLine();
                                Run(configArgs);
                                Console.WriteLine();
                            }
                        }
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e);
                        Console.WriteLine();
                    }
                    Console.WriteLine("Press any key to exit.");
                    Console.ReadKey();
                    FreeConsole();
                }
                else
                {
                    Run(args);
                }
            }
        }

        static void Run(IList<string> args)
        {
            if (!Directory.Exists("dist"))
            {
                throw new Exception($"Error: dist directory not found! Keep it in the same directory as esdtool.exe");
            }
            ESDOptions options;
            try
            {
                options = ESDOptions.Parse(args);
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
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
