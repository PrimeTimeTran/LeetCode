class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n+1)] for i in range(m+1)]    
        dp[1][1] = 1
        for i in range(m+1):
            for j in range(n+1):
                cur = dp[i][j]
                if i + 1 <= m:
                    dp[i+1][j] += cur
                if j + 1 <= n:
                    dp[i][j+1] += cur
        return dp[m][n]