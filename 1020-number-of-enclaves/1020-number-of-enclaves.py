class Solution:
    def numEnclaves(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out or (r,c) in seen or g[r][c] == 0:
                return 0
            seen.add((r,c))
            g[r][c] = 0
            
            
            
            

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        res = 0
        for r in range(m):
            for c in range(n):
                if g[r][c] and (r in [0, m-1] or c in [0, n-1]):
                    dfs(r,c)
                    
        for r in range(m):
            for c in range(n):
                if g[r][c]:
                    res += dfs(r,c)
        return res
            