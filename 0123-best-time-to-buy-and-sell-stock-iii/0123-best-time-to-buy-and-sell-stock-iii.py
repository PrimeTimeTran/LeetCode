from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i: int, completed_transactions: int, holding: bool) -> int:
            # Base cases
            if i == n or completed_transactions == 2:
                return 0 if not holding else -inf

            # Option 1: skip today
            skip = dp(i + 1, completed_transactions, holding)

            if holding:
                # Option 2: sell today
                sell = prices[i] + dp(i + 1, completed_transactions + 1, False)
                return max(skip, sell)
            else:
                # Option 2: buy today
                buy = -prices[i] + dp(i + 1, completed_transactions, True)
                return max(skip, buy)

        return dp(0, 0, False)

        # if not prices: return 0
        # # forward traversal, profits record the max profit 
        # # by the ith day, this is the first transaction
        # profits = []
        # max_profit = 0
        # current_min = prices[0]
        # for price in prices:
        #     current_min = min(current_min, price)
        #     max_profit = max(max_profit, price - current_min)
        #     profits.append(max_profit)
        
        # # backward traversal, max_profit records the max profit
        # # after the ith day, this is the second transaction 
        # total_max = 0    
        # max_profit = 0
        # current_max = prices[-1]
        # for i in range(len(prices) - 1, -1, -1):
        #     current_max = max(current_max, prices[i])
        #     max_profit = max(max_profit, current_max - prices[i])
        #     total_max = max(total_max, max_profit + profits[i])
            
        # return total_max