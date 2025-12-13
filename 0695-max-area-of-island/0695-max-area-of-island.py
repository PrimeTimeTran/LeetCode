class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res, seen, R, C = 0, set(), len(grid), len(grid[0])
        def dfs(r,c):
            safe = 0 <= r < R and 0 <= c < C
            if safe and (r,c) not in seen and grid[r][c] == 1:
                seen.add((r,c))
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res