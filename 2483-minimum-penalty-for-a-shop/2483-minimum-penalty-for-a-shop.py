class Solution:
    def bestClosingTime(self, S):
        ans = 0
        cur = cmin = S.count('Y')
        for e, i in enumerate(S):
            cur -= (1 if i == 'Y' else -1)
            if cur < cmin:
                ans, cmin = e + 1, cur
        return ans