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
            # If holding, sell, credit
            # If not holding, buy, debiting
            realized = price if holding else -price
            cooldown = holding
            pnl = realized + dp(i, not holding, cooldown)
            return max(skip, pnl)
        return dp(0, False, False)