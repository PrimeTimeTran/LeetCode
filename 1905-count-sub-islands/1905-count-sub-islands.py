'''
Iterate mat and DFS on land cells marking em all seen. If any twin cell in g1 is water return False.
Otherwise return check all cells of island in g2 is also land in g1.
'''

class Solution:
    def countSubIslands(self, g1: List[List[int]], g2: List[List[int]]) -> int:
        m,n = len(g2), len(g2[0])
        
        seen = set()
        def dfs(r,c):
            o = r < 0 or c < 0 or r == m or c == n or (r,c) in seen or g2[r][c] == 0
            if o:
                return True
            seen.add((r,c))
            res = True
            if g1[r][c] == 0:
                res = False
            res = dfs(r+1,c) and res
            res = dfs(r-1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res
            return res
            
        res = 0
        for r in range(m):
            for c in range(n):
                if g2[r][c] and (r,c) not in seen and dfs(r,c):
                    res+=1
        return res