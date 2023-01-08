d = [0,1,0,-1,0]
class Solution:
    def wallsAndGates(self, g: List[List[int]]) -> None:
        m, n= len(g), len(g[0])
        def bfs(r,c):
            q = deque([])
            for i in range(4):
                q.append([r+d[i],c+d[i+1], 1])
            seen = set()
            while q:
                x, y, val = q.popleft()
                out  = x < 0 or x == m or y < 0 or y == n
                if out or g[x][y] in [0, -1] or (x, y) in seen:
                    continue
                seen.add((x, y))
                g[x][y] = min(g[x][y], val)
                for i in range(4):
                    q.append([x+d[i],y+d[i+1], val+1])
            
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    bfs(r,c)