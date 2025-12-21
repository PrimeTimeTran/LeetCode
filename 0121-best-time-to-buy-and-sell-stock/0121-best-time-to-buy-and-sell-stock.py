'''
1. Understand
Return the best profit you can make given a list of prices of stocks on a range of days.
You can make at most one transaction and can only profit when you buy & then sell a stock.

State Machine:
- Day purchaseed and remaining.
- Whether or not holding a stock(previously purchased).

Pseudocode:
From the first day skip and take the day until you've reached the end of the list.
Inside of recursion, compare which was more profitable. Taking or selling.
When moving forward track whether or not you bought/sold so you can know when you need to do on subsequent days.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, open):
            if i == n:
                return 0
            price = prices[i]
            i+=1
            skip = dp(i, open)
            if open:
                act = price
            else:
                act = -price + dp(i, True)
            return max(skip, act)

        return dp(0, False)