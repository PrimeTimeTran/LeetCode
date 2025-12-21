class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0
            skip = dp(i + 1, holding)
            sign = 1 if holding else -1
            price = prices[i]
            pnl = sign * price
            if not holding:
                pnl = pnl + dp(i + 1, True)
            return max(skip, pnl)

        return dp(0, False)