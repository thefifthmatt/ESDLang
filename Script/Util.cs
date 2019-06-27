using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ESDLang.Script
{
    public class Util
    {
        public static void AddMulti<K, V>(IDictionary<K, List<V>> dict, K key, V value)
        {
            if (!dict.ContainsKey(key)) dict[key] = new List<V>();
            dict[key].Add(value);
        }
        public static void AddMulti<K, V>(IDictionary<K, List<V>> dict, K key, IEnumerable<V> values)
        {
            if (!dict.ContainsKey(key)) dict[key] = new List<V>();
            dict[key].AddRange(values);
        }
        public static void AddMulti<K, V>(IDictionary<K, HashSet<V>> dict, K key, V value)
        {
            if (!dict.ContainsKey(key)) dict[key] = new HashSet<V>();
            dict[key].Add(value);
        }
        public static void AddMulti<K, V>(IDictionary<K, HashSet<V>> dict, K key, IEnumerable<V> values)
        {
            if (!dict.ContainsKey(key)) dict[key] = new HashSet<V>();
            dict[key].UnionWith(values);
        }
        public static void AddMulti<K, V>(IDictionary<K, SortedSet<V>> dict, K key, V value)
        {
            if (!dict.ContainsKey(key)) dict[key] = new SortedSet<V>();
            dict[key].Add(value);
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
    }
}
