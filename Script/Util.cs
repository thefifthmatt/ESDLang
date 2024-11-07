using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ESDLang.Script
{
    public class Util
    {
        public static void AddMulti<K, V, T>(IDictionary<K, T> dict, K key, V value)
            where T : ICollection<V>, new()
        {
            if (!dict.TryGetValue(key, out T col))
            {
                dict[key] = col = new T();
            }
            col.Add(value);
        }

        public static void AddMulti<K, V, T>(IDictionary<K, T> dict, K key, IEnumerable<V> values)
            where T : ICollection<V>, new()
        {
            if (!dict.TryGetValue(key, out T col))
            {
                dict[key] = col = new T();
            }
            if (col is ISet<V> set)
            {
                set.UnionWith(values);
            }
            else if (col is List<V> list)
            {
                list.AddRange(values);
            }
            else
            {
                foreach (V value in values)
                {
                    col.Add(value);
                }
            }
        }

        public static void AddMulti<K, V, V2, T>(IDictionary<K, T> dict, K key, V value, V2 value2)
            where T : IDictionary<V, V2>, new()
        {
            if (!dict.ContainsKey(key)) dict[key] = new T();
            dict[key][value] = value2;
        }

        public static void AddMultiNest<K, V, V2, T>(IDictionary<K, T> dict, K key, V value, V2 value2)
            where T : IDictionary<V, List<V2>>, new()
        {
            // List<V2> cannot be generic because C# can't this level of inference
            if (!dict.ContainsKey(key)) dict[key] = new T();
            AddMulti(dict[key], value, value2);
        }

        public static void AddMultiNestSet<K, V, V2, T>(IDictionary<K, T> dict, K key, V value, V2 value2)
            where T : IDictionary<V, SortedSet<V2>>, new()
        {
            // List<V2> cannot be generic because C# can't this level of inference
            if (!dict.ContainsKey(key)) dict[key] = new T();
            AddMulti(dict[key], value, value2);
        }

        public static List<List<T>> MultiCartesian<T>(List<List<T>> sets, int consumed=0)
        {
            if (sets.Count <= consumed)
            {
                return new List<List<T>>();
            }
            else if (sets.Count - consumed == 1)
            {
                return sets[0].Select(e => new List<T> { e }).ToList();
            }
            else
            {
                List<T> last = sets[sets.Count - 1 - consumed];
                List<List<T>> ret = new List<List<T>>();
                foreach (List<T> prefix in MultiCartesian(sets, consumed + 1))
                {
                    foreach (T suffix in last)
                    {
                        ret.Add(prefix.Concat(new[] { suffix }).ToList());
                    }
                }
                return ret;
            }
        }

        public static string WindowsifyPath(string path)
        {
            if (path == null) return null;
            if (path.StartsWith("/mnt/"))
            {
                string drive = path[5].ToString();
                return $"{drive.ToUpper()}:{path.Substring(6)}";
            }
            return path;
        }
    }
}
