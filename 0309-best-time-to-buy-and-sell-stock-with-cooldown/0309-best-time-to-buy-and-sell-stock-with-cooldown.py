from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, open_position, cooldown):
            if i == len(prices):
                return 0 if open_position is not "buy_to_open" else -inf
            price = prices[i]
            i+=1
            if cooldown:
                return dp(i, None, None)
            if open_position == "buy_to_open":
                sell_today = price + dp(i, None, True)
                hold_today = dp(i, open_position, None)
                return max(sell_today, hold_today)
            else:
                buy_today  = -price + dp(i, "buy_to_open", None)
                skip_today = dp(i, None, None)
                return max(buy_today, skip_today)
        return dp(0, None, None)
