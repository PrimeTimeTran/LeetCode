from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        FREE, HOLD = 0, 1
        @lru_cache(None)
        def dp(i, state):
            if i == len(prices):
                return 0 if state is not HOLD else -inf
            price = prices[i]
            i+=1
            if state == FREE:
                return max(
                    dp(i, HOLD) - price,
                    dp(i, FREE)
                )
            elif state == HOLD:
                return max(
                    dp(i, None) + price,
                    dp(i, HOLD)
                )
            return dp(i, FREE)

        return dp(0, FREE)
