class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i: int, is_holding: bool, is_cooldown: bool) -> int:
            if i == n: return 0
            i, price = i + 1, prices[i]
            skip = dp(i, is_holding, False)
            if is_cooldown: return skip
            pnl = price if is_holding else -price
            # is_cooldown = is_holding
            realized = pnl + dp(i, not is_holding, is_holding)
            return max(skip, realized)
        return dp(0, False, False)
