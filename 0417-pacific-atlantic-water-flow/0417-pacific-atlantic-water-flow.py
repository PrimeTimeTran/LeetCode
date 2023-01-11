'''
Find cells reachable by each ocean working outside in.
If a cell is reachable by both oceans add to res.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,atl = set(), set()
        m,n = len(heights), len(heights[0])
        
        def dfs(seen, r, c, p):
            o = r < 0 or c < 0 or r == m or c == n
            if o or p > heights[r][c] or (r,c) in seen:
                return
            
            seen.add((r,c))
            cur = heights[r][c]
            dfs(seen, r+1, c, cur)
            dfs(seen, r-1, c, cur)
            dfs(seen, r, c+1, cur)
            dfs(seen, r, c-1, cur)
            
        
        for r in range(m):
            dfs(atl, r, n-1, heights[r][n-1])    
            dfs(pac, r, 0, heights[r][0])        
            
        for c in range(n):
            dfs(atl, m-1, c, heights[m-1][c])        
            dfs(pac, 0, c, heights[0][c])    
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        
        return res
        
        