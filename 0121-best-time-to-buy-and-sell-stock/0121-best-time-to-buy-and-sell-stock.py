class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = l = 0
        for r, p in enumerate(prices):
            ans = max(ans, p - prices[l])
            if p < prices[l]: l = r
        return ans