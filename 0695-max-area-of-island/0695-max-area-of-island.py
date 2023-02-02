class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        seen = set()
        def dfs(r,c):
            inbounds = 0 <= r < m and 0 <= c < n
            if inbounds and (r,c) not in seen and grid[r][c]:
                seen.add((r,c))
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0
            
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    res = max(res, dfs(r,c))
                    
        return res