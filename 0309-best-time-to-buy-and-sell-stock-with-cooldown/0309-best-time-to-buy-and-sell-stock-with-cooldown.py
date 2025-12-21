class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, holding: bool, cooldown: bool) -> int:
            if i == len(prices): return 0
            price = prices[i]
            i += 1
            skip = dp(i, holding, False)
            if cooldown:
                return skip
            realized = price if holding else -price
            if holding:
                pnl = realized + dp(i, not holding, True)
            else:
                pnl = realized + dp(i, not holding, False)
            return max(skip, pnl)
        return dp(0, False, False)