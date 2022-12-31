class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r < 0 or c < 0:
                return 0
            if r == 1 and c == 1:
                return 1
            memo[(r,c)] = dfs(r-1,c) + dfs(r,c-1)
            return memo[(r,c)]
        return dfs(m,n)