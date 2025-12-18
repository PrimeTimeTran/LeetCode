class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,rem):
            if i == len(prices) or rem == 0:
                return 0
            skip = dp(i+1, rem)
            future = dp(i+1, rem-1)
            # Apply buy/sell sign
            # Even number transactions means debit(-)
            # Odd  number transactions means credit(+)
            sign = -1 if rem % 2 == 0 else 1
            take = future + sign * prices[i]
            return max(skip, take)
        return dp(0, k * 2)

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         # bottom up 
#         dp = [0]*((k*2)+1)

#         for i in range(len(prices)-1,-1,-1):
#             next_dp = [0]*((k*2)+1)

#             for j in range(1,(k*2)+1):
#                 col = (k*2) - j
#                 if j%2 == 1:
#                     # sell the stock or skip
#                     next_dp[col] = max(dp[col],prices[i]+dp[col+1])
#                     continue
#                 next_dp[col] = max(dp[col],-prices[i]+dp[col+1])
#             dp = next_dp
#         print(dp)
#         return dp[0]
        