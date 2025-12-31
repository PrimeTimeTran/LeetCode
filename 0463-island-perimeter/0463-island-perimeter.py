class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen, self.ans, R, C = set(), 0, len(grid), len(grid[0])
        def dfs(r, c):
            if (r,c) in seen: return
            safe = 0 <= r < R and 0 <= c < C
            if not safe or grid[r][c] == 0:
                self.ans += 1
            else:
                seen.add((r,c))
                for dr, dc in [r+1,c], [r-1,c], [r,c+1], [r,c-1]:
                    dfs(dr, dc)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    dfs(r, c)
        return self.ans