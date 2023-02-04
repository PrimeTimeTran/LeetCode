class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        
        res = 0
        seen = set()
        
        def dfs(r,c):
            inbounds = 0 <= r < m and 0 <= c < n
            if inbounds and grid[r][c] == "1" and (r,c) not in seen:
                seen.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
                return True
            return False
                
        for r in range(m):
            for c in range(n):
                if dfs(r,c):
                    res+=1
        return res
        
        