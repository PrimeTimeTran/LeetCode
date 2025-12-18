class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def dp(i: int, transactions_completed: int):
            if i == len(prices) or transactions_completed == k*2:
                return 0
            p = prices[i]
            i += 1
            sign = -1 if transactions_completed % 2 == 0 else 1
            pnl_today = sign * p

            pnl_unrealized = dp(i, transactions_completed + 1)
            pnl_today_included = pnl_today + pnl_unrealized

            pnl_today_skipped = dp(i, transactions_completed)
            return max(pnl_today_included, pnl_today_skipped)
        return dp(0, 0)

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
        