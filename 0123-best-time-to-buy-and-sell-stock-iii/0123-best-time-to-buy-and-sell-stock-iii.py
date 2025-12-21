from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @lru_cache(None)
        # def dp(i: int, completed_count: int, open_position: bool) -> int:
        #     if i == len(prices) or completed_count == 2:
        #         return -inf if open_position else 0
        #     price = prices[i]
        #     i+=1
        #     pnl_today_excluded = dp(i, completed_count, open_position)
        #     if open_position:
        #         pnl_today_included = price + dp(i, completed_count + 1, False)
        #     else:
        #         pnl_today_included = -price + dp(i, completed_count, True)
        #     return max(pnl_today_excluded, pnl_today_included)

        # return dp(0, 0, False)

        # if not prices: return 0
        # # forward traversal, profits record the max profit 
        # # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
        
        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction 
        total_max = 0    
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
            
        return total_max