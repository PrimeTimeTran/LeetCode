class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        dp[0] = [prices[0],0]
        min_price = max_profit = 0
        for i in range(1,n):
            min_price = min(dp[i-1][0], prices[i])
            max_profit = max(dp[i-1][1], prices[i]-dp[i-1][0])
            dp[i] =[min_price,max_profit]
                
        return dp[n-1][1]
