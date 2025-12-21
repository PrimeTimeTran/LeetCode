class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0
            if holding:
                sell = prices[i]        # profit from selling today
                skip = dp(i + 1, True)
                return max(skip, sell)
            else:
                buy  = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)
                return max(skip, buy)

        return dp(0, False)