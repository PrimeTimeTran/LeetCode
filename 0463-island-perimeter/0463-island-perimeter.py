class Solution:
    def islandPerimeter(self,g: List[List[int]]) -> int:
        m,n=len(g), len(g[0])
        
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n 
            if out or g[r][c] == 0:
                return 1
            if (r,c) in seen:
                return 0
            seen.add((r,c))
            
            return dfs(r+1,c) +dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(m):
            for c in range(n):
                if g[r][c]:
                    return dfs(r,c)