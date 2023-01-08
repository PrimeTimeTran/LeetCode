class Solution:
    def wallsAndGates(self, g: List[List[int]]) -> None:
        if not g:
            return 
        m, n= len(g), len(g[0])
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    queue = deque([])
                    queue.append((r+1, c, 1)); queue.append((r-1, c, 1))
                    queue.append((r, c+1, 1)); queue.append((r, c-1, 1))
                    seen = set()
                    while queue:
                        x, y, val = queue.popleft()
                        out  = x < 0 or x >= m or y < 0 or y >= n
                        if out or g[x][y] in [0, -1] or (x, y) in seen:
                            continue
                        seen.add((x, y))
                        g[x][y] = min(g[x][y], val)
                        queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                        queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))