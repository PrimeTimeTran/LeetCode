class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                pro += prices[i] - prices[i-1]
        return pro