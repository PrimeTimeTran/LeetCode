class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            groups[tuple(sorted(w))].append(w)
        return list(groups.values())
