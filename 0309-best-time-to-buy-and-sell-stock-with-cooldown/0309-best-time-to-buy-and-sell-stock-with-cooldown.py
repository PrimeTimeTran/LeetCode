from functools import lru_cache
from math import inf
from typing import List, Union

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, open_position: Union[str, bool], cooldown):
            if i == len(prices):
                return 0 if not open_position else -inf
            price = prices[i]
            i+=1

            if cooldown:
                return dp(i, open_position, False)

            if open_position:
                pnl_today_included = price + dp(i, None, True)
                pnl_today_skipped = dp(i, open_position, False)
            else:
                pnl_today_included  = -price + dp(i, True, False)
                pnl_today_skipped = dp(i, None, False)
            return max(pnl_today_included, pnl_today_skipped)

        return dp(0, None, False)
