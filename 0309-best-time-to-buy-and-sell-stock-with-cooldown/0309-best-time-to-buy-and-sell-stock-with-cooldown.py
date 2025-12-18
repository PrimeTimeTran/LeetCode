from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, open_position: Union[str, bool], cooldown):
            if i == len(prices):
                return 0 if open_position != "buy_to_open" else -inf
            price = prices[i]
            i+=1
            if cooldown:
                return dp(i, open_position, False)
            if open_position == "buy_to_open":
                pnl_from_close = price + dp(i, None, True)
                pnl_from_holding = dp(i, open_position, False)
                return max(pnl_from_close, pnl_from_holding)
            else:
                pnl_from_opening  = -price + dp(i, "buy_to_open", False)
                pnl_from_waiting = dp(i, None, False)
                return max(pnl_from_opening, pnl_from_waiting)
        return dp(0, False, False)
