class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = maxf = 0
        w = {}
        for r, c in enumerate(s):
            w[c] = w.get(c, 0) + 1
            maxf = max(maxf, w[c])
            while (r-l+1) - maxf > k:
                w[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res