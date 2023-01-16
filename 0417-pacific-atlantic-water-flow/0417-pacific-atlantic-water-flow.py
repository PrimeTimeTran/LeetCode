'''
Iterate mat borders and DFS each cell if prev value is less than upcoming value.
Add cells reachable by both oceans to sets representing both oceans.
Iterate mat and add cells reachable by both oceans to res list and return it.
'''

class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        pac,atl = set(), set()
        m,n = len(h), len(h[0])
        
        def dfs(seen, r,c, prev):
            o = r < 0 or c < 0 or r == m or c == n
            if o or (r,c) in seen:
                return 
            cur = h[r][c]
            if prev > cur: return
            seen.add((r,c))
            
            dfs(seen, r+1,c,cur)
            dfs(seen, r-1,c,cur)
            dfs(seen, r,c+1,cur)
            dfs(seen, r,c-1,cur)
        
        
        for r in range(m):
            dfs(pac,r, 0, h[r][0])
            dfs(atl,r, n-1, h[r][n-1])
            
        for c in range(n):
            dfs(pac,0, c, h[0][c])
            dfs(atl,m-1, c, h[m-1][c])

        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
        return res