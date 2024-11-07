using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NativeFileDialogSharp;

namespace ESDLang.Script
{
    public class FileDialog
    {
        public static bool OpenFileDialog(IReadOnlyList<string> filters, out string path, string defaultPath = null)
        {
            DialogResult dialogResult = Dialog.FileOpen(CombineFilters(filters, false), defaultPath);
            path = dialogResult.Path;
            return dialogResult.IsOk;
        }

        public static bool OpenMultiFileDialog(IReadOnlyList<string> filters, out IReadOnlyList<string> paths, string defaultPath = null)
        {
            DialogResult dialogResult = Dialog.FileOpenMultiple(CombineFilters(filters, false), defaultPath);
            paths = dialogResult.Paths;
            return dialogResult.IsOk;
        }

        public static bool SaveFileDialog(IReadOnlyList<string> filters, out string path, string defaultPath = null)
        {
            DialogResult dialogResult = Dialog.FileSave(CombineFilters(filters, true), defaultPath);
            path = dialogResult.Path;
            return dialogResult.IsOk;
        }

        public static bool OpenFolderDialog(out string path, string defaultPath = null)
        {
            DialogResult dialogResult = Dialog.FolderPicker(defaultPath);
            path = dialogResult.Path;
            return dialogResult.IsOk;
        }

        private static string CombineFilters(IReadOnlyList<string> filters, bool dropdown)
        {
            return filters.Count == 0 ? null : string.Join(dropdown ? ";" : ",", filters);
        }
    }
}
