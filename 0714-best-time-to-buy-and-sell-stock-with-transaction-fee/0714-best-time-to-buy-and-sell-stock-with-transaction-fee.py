'''
1. Understand
Find maximum profit attainable from given prices where a completed transaction is charged a fee.
You must buy and sell to realize a profit.
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0
            price = prices[i]
            i+=1
            skip = dp(i, holding)
            unrealized = dp(i, not holding)
            pnl = price - fee if holding else -price
            return max(skip, pnl + unrealized)
        return dp(0, False)
