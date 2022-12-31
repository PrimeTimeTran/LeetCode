class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r < 0 or c < 0:
                return 0
            if obstacleGrid[r-1][c-1] == 1:
                return 0
            if r == 1 and c == 1:
                return 1
            memo[(r,c)] = dfs(r-1,c) + dfs(r,c-1)
            return memo[(r,c)]
            
        return dfs(m,n)    