class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for w in strs:
        res[tuple(sorted(w))].append(w)
    return list(res.values())