from functools import lru_cache
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: bool) -> int:
            if i == n:
                return -inf if holding else 0

            price = prices[i]

            if holding:
                skip = dp(i + 1, True)
                sell = price
                return max(skip, sell)
            else:
                skip = dp(i + 1, False)
                buy  = -price + dp(i + 1, True)
                return max(skip, buy)

        return dp(0, False)
