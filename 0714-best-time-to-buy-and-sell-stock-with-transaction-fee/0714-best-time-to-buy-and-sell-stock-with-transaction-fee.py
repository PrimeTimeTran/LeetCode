from functools import lru_cache
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0
            
            price = prices[i]
            
            if holding:
                # Option 1: sell today
                sell = price - fee + dp(i+1, False)
                # Option 2: skip / hold
                hold = dp(i+1, True)
                return max(sell, hold)
            else:
                # Option 1: buy today
                buy = -price + dp(i+1, True)
                # Option 2: skip
                skip = dp(i+1, False)
                return max(buy, skip)
        
        return dp(0, False)
