class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]   # best profit after buying once
        sell = 0           # best profit after selling once

        for price in prices[1:]:
            buy = max(buy, -price)        # buy ONCE
            sell = max(sell, buy + price) # sell ONCE

        return sell
