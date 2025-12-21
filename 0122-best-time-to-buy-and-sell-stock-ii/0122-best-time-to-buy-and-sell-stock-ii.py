class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0, -prices[0]]
        for price in prices[1:]:
            new_dp = [-inf, -inf]
            new_dp[0] = max(new_dp[0], dp[0])
            new_dp[1] = max(new_dp[1], dp[1])
            new_dp[1] = max(new_dp[1], dp[0] - price)
            new_dp[0] = max(new_dp[0], dp[1] + price)
            dp = new_dp
        return dp[0]
