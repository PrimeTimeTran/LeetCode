class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 1
            if prices[i] == prices[i-1] - 1:
                return dp(i-1) + 1
            return 1

        return sum(dp(i) for i in range(n))
