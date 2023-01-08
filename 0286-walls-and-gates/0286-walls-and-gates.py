class Solution:
    def wallsAndGates(self, g: List[List[int]]) -> None:
        if not g:
            return 
        m, n= len(g), len(g[0])
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    q = deque([])
                    q.append((r+1, c, 1)); q.append((r-1, c, 1))
                    q.append((r, c+1, 1)); q.append((r, c-1, 1))
                    seen = set()
                    while q:
                        x, y, val = q.popleft()
                        out  = x < 0 or x >= m or y < 0 or y >= n
                        if out or g[x][y] in [0, -1] or (x, y) in seen:
                            continue
                        seen.add((x, y))
                        g[x][y] = min(g[x][y], val)
                        q.append((x+1, y, val+1)); q.append((x-1, y, val+1))
                        q.append((x, y+1, val+1)); q.append((x, y-1, val+1))