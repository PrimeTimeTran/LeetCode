class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        
        
        def dfs(r,c,prev):
            out = r < 0 or c < 0 or r == m or c == n or matrix[r][c] <= prev
            if out:
                return 0 
            if dp[r][c] != -1:
                return dp[r][c]
            
            p = matrix[r][c]
            
            t = max(
                dfs(r+1,c,p),
                dfs(r-1,c,p),
                dfs(r,c+1,p),
                dfs(r,c-1,p)
            )
            
            dp[r][c] = t + 1
            return dp[r][c]
       
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r,c, -1))
        return res