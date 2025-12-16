class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, cur, res, seen = 0, 0, 0, set()
        for r, c in enumerate(s):
            while c in seen:
                if s[l] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(c)
            res = max(res, r - l + 1)
        return res