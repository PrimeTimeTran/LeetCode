class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,rem):
            if i == len(prices) or rem == 0:
                return 0

            sign = -1 if rem % 2 == 0 else 1
            pnl_today = sign * prices[i]

            pnl_unrealized = dp(i+1, rem - 1)
            pnl_today_included = pnl_today + pnl_unrealized

            pnl_today_excluded = dp(i + 1, rem)
            return max(pnl_today_included, pnl_today_excluded)
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
        