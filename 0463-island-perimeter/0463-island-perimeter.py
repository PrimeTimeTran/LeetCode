'''
Traverse using nested loops calling DFS land cell.
In DFS, guard for out or water, returning 1; the addition to perimeter.
If DFS cell in seen, return 0.
Return recursive sum of DFS called on neighbors.
'''
class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out or g[r][c] == 0: return 1
            if (r,c) in seen: return 0
            seen.add((r,c))
            res = 0
            d = [0,1,0,-1,0]
            for i in range(4):
                nr, nc = r + d[i], c + d[i+1]
                res += dfs(nr, nc)
            return res
        
        for r in range(m):
            for c in range(n):
                if g[r][c]:
                    return dfs(r,c)