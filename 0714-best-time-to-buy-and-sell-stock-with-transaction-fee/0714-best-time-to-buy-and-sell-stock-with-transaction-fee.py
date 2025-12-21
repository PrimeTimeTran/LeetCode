class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        buy = float('-inf')
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell