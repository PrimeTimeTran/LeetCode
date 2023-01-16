'''
DFS 
DFS cells finding 1s. Mark adj 1 cells as seen and increment count.
'''
class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        m,n = len(g), len(g[0])
        seen = set()
        def dfs(r,c):
            o = r < 0 or c < 0 or r == m or c == n
            if o or (r,c) in seen or g[r][c] == "0":
                return
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        res = 0
        for r in range(m):
            for c in range(n):
                if g[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    res+=1
        return res