class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0  # always return 0 at the end

            if holding:
                # Either sell today or skip
                sell = prices[i]  # profit from selling today
                skip = dp(i + 1, True)
                # If we sell, we cannot sell again, so the recursion for future is 0
                return max(skip, sell)
            else:
                # Either buy today or skip
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)
                return max(skip, buy)

        return dp(0, False)
