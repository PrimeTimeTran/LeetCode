# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = res = 0
#         for r, p in enumerate(prices):
#             if prices[l] < p:
#                 l = r
#             else:
#                 res += p - prices[l]
#         return res