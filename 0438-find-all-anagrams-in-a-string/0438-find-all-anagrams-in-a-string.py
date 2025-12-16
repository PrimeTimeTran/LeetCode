class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, res, w = 0, [], {}
        sought = sorted(p)
        for r in range(len(s)):
            if r - l + 1 == len(p):
                if sought == sorted(s[l:r+1]):
                    res.append(l)
                l+=1
        return res