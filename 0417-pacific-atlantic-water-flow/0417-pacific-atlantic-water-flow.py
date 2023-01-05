'''
Using two sets, mark cells which can be reached by pac and atl oceans.
If the cell can be reached by both pac and atl add it to the res.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        
        
        def dfs(seen, r, c, prev):
            out = r < 0 or c < 0 or r == m or c == n
            if out:
                return 
            if prev > heights[r][c]:
                return
            if (r,c) in seen:
                return
            seen.add((r,c))
            cur = heights[r][c]
            dfs(seen, r+1,c,cur)
            dfs(seen, r-1,c,cur)
            dfs(seen, r,c+1,cur)
            dfs(seen, r,c-1,cur)
            
        
        
        pac, atl = set(), set()
        for r in range(m):
            dfs(pac,r,0,heights[r][0])    
            dfs(atl,r,n-1,heights[r][n-1])    
        
        for c in range(n):
            dfs(pac,0,c,heights[0][c])    
            dfs(atl,m-1,c,heights[m-1][c])    
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
        
        return res