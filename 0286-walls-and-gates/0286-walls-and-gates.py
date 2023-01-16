class Solution:
    def wallsAndGates(self, g: List[List[int]]) -> None:
        d = [0,1,0,-1,0]
        m, n = len(g), len(g[0])
        def bfs(r,c):
            q = deque([])
            for i in range(4):
                q.append([r+d[i],c+d[i+1], 1])
            seen = set()
            while q:
                r, c, val = q.popleft()
                out  = r < 0 or r == m or c < 0 or c == n
                if out or g[r][c] in [0, -1] or (r, c) in seen:
                    continue
                seen.add((r, c))
                g[r][c] = min(g[r][c], val)
                for i in range(4):
                    q.append([r+d[i],c+d[i+1], val+1])
            
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    bfs(r,c)