class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r, price in enumerate(prices):
            profit = price - prices[l]
            if price < prices[l]:
                l = r
            res = max(res, profit)
        return res
