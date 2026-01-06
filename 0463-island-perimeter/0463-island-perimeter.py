class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.res, seen = 0, set()
        def dfs(r,c):
            if (r,c) in seen: return 0
            inbounds = 0 <= r < R and 0 <= c < C
            if not inbounds or grid[r][c] == 0:
                return 1
            seen.add((r,c))
            val = 0
            for dr, dc in [r+1,c],[r-1, c],[r,c+1],[r,c-1]:
                val += dfs(dr, dc)
            self.res = max(self.res, val)
            return val
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    dfs(r,c)
        return self.res