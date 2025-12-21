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
            skip = dp(i+1, holding)
            if holding:
                sell = price - fee + dp(i+1, False)
                return max(sell, skip)
            else:
                buy = -price + dp(i+1, True)
                return max(buy, skip)
        return dp(0, False)
