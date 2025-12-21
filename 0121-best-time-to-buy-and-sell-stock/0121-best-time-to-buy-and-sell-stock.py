from functools import lru_cache
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return 0 if not holding else -inf

            price = prices[i]

            if not holding:
                skip = dp(i + 1, False)
                buy  = -price + dp(i + 1, True)
                return max(skip, buy)
            else:
                skip = dp(i + 1, True)
                sell = price        # once sold, transaction is complete
                return max(skip, sell)

        return dp(0, False)
