class Solution:
    def uniquePaths(self, m: int, n: int, dic = {}) -> int:
        if (m,n) in dic:
            return dic[(m,n)]
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        dic[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m,n-1)
        return dic[(m,n)]
    
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