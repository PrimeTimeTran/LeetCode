# class Solution:
#     def maxProfit(self, P: List[int]) -> int:
#         ans,l = 0, 0
#         for r, n in enumerate(P):
#             ans = max(ans, n - P[l])
#             if n < P[l]: l = r
#         return ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = l = 0
        for r, n in enumerate(prices):
            ans = max(ans, n - prices[l])
            if n < prices[l]: l = r
        return ans