'''
Create a 2d matrix using m and n as a cache for DP to avoid TLE.
Iterate all cells with m and n. Check for new max length path using DFS passing dfs previous cell value.
In conjunction with checking next cell out of bounds, check if next cell less than or equal to previous cell, if so return 0.

Check for memoized value and return if found.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(r,c,p):
            out = r < 0 or c < 0 or r == m or c == n or matrix[r][c] <= p
            if out:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            cur = matrix[r][c]
            
            t = max(
                dfs(r+1,c,cur),
                dfs(r-1,c,cur),
                dfs(r,c+1,cur),
                dfs(r,c-1,cur)
            )
            dp[r][c] = 1 + t
            return dp[r][c]
        
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r,c,-1))
                
        return res