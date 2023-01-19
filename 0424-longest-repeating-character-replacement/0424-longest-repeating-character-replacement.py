class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win, l = {}, 0
        maxf, res = 0,0
        for r, c in enumerate(s):
            win[c] = win.get(c,0) +1
            maxf = max(maxf, win[c])
            while (r-l+1) - maxf > k:
                win[s[l]] -= 1
                l+=1
        res = max(r-l+1, res)
        return res

