class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        seen = set()
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l+=1
            seen.add(c)
            res = max(r - l + 1, res)
        return res