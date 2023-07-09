class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res, l = 0, 0
        for r, c in enumerate(s):
            cur = s[l:r+1]
            while len(list(set(cur))) > k:
                l+=1
                cur = s[l:r+1]
            res = max(res, r-l+1)
        return res