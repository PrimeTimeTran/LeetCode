'''
Loop grid performing DFS on any land found. 
DFS marks all land cells neighboring as seen and returns the sum of recursive calls.
'''

class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out: return 0
            if g[r][c] == 0 or (r,c) in seen:
                return 0
            seen.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(dfs(r,c), res)
        return res