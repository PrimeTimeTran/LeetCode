class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.res, seen = 0, set()
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1: 
                return 0
            grid[r][c] = -1
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    return dfs(r,c)