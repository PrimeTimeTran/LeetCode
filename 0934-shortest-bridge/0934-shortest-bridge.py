class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        seen = set()
        DIR = [0,1,0,-1,0]
        m, n = len(grid), len(grid[0])
        
        def out(r,c): return not (0 <= r < m and 0 <= c < n)
        
        def dfs(r, c):
            seen.add((r, c))
            
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                if out(nr,nc) or (nr, nc) in seen or not grid[r][c]:
                    continue
                dfs(nr, nc)
        
        r, c = next((r, c) for r in range(m) for c in range(n) if grid[r][c] == 1)
        dfs(r, c)
        
        level = 1
        q = deque(seen)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r+DIR[i], c+DIR[i+1]
                    if (nr, nc) in seen or out(nr,nc):
                        continue
                    if grid[nr][nc] == 1:
                        return level
                    
                    seen.add((nr, nc))
                    q.append((nr, nc))
            level += 1
        return -1