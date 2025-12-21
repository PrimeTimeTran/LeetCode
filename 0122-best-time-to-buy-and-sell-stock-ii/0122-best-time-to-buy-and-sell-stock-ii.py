'''
1. Understand
Given a list of stock prices return the total profit you can make buying and selling.
You must first buy a stock to sell it.

Pseudocode:
From first day skip and take that day and then proceed to further days.
Taking is a relative term, you must sell after buying and buy before selling.

Recurse by moving forward in the list of days and exiting when you've reached the base case(last day).
Depending on if you're selling or buying, you will ± price.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, holding):
            if i == n:
                return 0
            skip = dp(i+1, holding)
            price = prices[i]
            if holding:
                sell = price + dp(i+1, False)
                return max(skip, sell)
            else:
                buy = -price + dp(i+1, True)
                return max(skip, buy)
        return dp(0, False)