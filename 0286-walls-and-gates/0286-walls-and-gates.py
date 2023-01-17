class Solution:
    def wallsAndGates(self, g: List[List[int]]) -> None:
        m,n = len(g), len(g[0])
        d = [0,-1,0,1,0]
        
        def bfs(r,c):
            q = deque([])
            for i in range(4):
                nr,nc = r+d[i],c+d[i+1]
                q.append((nr,nc,1))
            seen = set()
            while q:
                r, c, v = q.popleft()
                o = r < 0 or c < 0 or r == m or c == n
                if o  or g[r][c] in [-1, 0] or (r,c) in seen:
                    continue
                seen.add((r,c))
                g[r][c] = min(g[r][c], v)
                for i in range(4):
                    nr,nc = r+d[i],c+d[i+1]
                    q.append((nr,nc,1+v))
        
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    bfs(r,c)
                    
        return g
        