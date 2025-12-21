class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, holding, transaction_count):
            if i == n or transaction_count == 2:
                return 0
            skip = dp(i+1, holding, transaction_count)
            sign = 1 if holding else -1
            pnl = sign * prices[i]
            transaction_count += 1 if holding else 0
            buy_or_sell = pnl + dp(i+1, not holding, transaction_count)
            return max(skip, buy_or_sell)
        return dp(0, False, 0)