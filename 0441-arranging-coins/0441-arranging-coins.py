class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 1
        r_count = 0
        while n > 0:
            r = r + 1
            n -= r
            r_count+=1
        return r_count