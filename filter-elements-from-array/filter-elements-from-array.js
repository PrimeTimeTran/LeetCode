/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
  const vals = []
  for (const idx of arr.keys()) {
    if (fn(arr[idx], idx)) vals.push(arr[idx])
  }
  return vals
};