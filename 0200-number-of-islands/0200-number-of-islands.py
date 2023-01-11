class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        m,n = len(g), len(g[0])
        
        seen = set()
        def dfs(r,c):
            o = r < 0 or c < 0 or r == m or c == n
            if o:
                return False
            if (r,c) in seen or g[r][c] == "0":
                return False 
            seen.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
            
        res = 0
        for r in range(m):
            for c in range(n):
                if dfs(r,c):
                    res+=1
        return res