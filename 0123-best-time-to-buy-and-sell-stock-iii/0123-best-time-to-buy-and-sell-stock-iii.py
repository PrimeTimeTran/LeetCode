class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i: int, count_transactions: int, position_open: bool) -> int:
            if i == n or count_transactions == 2:
                return 0

            price = prices[i]

            # Skip today
            pnl_today_skipped = dp(i + 1, count_transactions, position_open)

            if position_open:
                # Option to sell today (if we can)
                sell = price + dp(i + 1, count_transactions + 1, False)
                return max(pnl_today_skipped, sell)
            else:
                # Option to buy today
                buy = -price + dp(i + 1, count_transactions, True)
                return max(pnl_today_skipped, buy)

        return dp(0, 0, False)


        # 2. Bottom Up
        # dp[k][h]: max profit with k transactions, holding h
        # dp = [[-inf, -inf] for _ in range(3)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]

        # for price in prices[1:]:
        #     new_dp = [[-inf, -inf] for _ in range(3)]
        #     for k in range(3):
        #         # skip
        #         new_dp[k][0] = max(new_dp[k][0], dp[k][0])
        #         new_dp[k][1] = max(new_dp[k][1], dp[k][1])

        #         # buy
        #         if dp[k][0] != -inf:
        #             new_dp[k][1] = max(new_dp[k][1], dp[k][0] - price)

        #         # sell
        #         if k > 0 and dp[k-1][1] != -inf:
        #             new_dp[k][0] = max(new_dp[k][0], dp[k-1][1] + price)

        #     dp = new_dp
        # print(dp)
        # return max(dp[k][0] for k in range(3))
