# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         maxf, res, l, win = 0, 0, 0, {}
#         for r, c in enumerate(s):
#             win[c] = win.get(c, 0) + 1
#             maxf = max(maxf, win[c])
#             while (r - l + 1) - maxf > k:
#                 win[s[l]] -= 1
#                 l += 1
#             res = max(res, r - l + 1)
#         return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, res, l, win = 0, 0, 0, {}
        for r, c in enumerate(s):
            win[c] = win.get(c, 0) + 1
            maxf = max(maxf, win[c])
            while (r-l+1) - maxf > k:
                win[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res
        