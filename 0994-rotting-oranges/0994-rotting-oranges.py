class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0]) 
        f, q = 0, deque()
        
        for r in range(m):
            for c in range(n):
                if g[r][c] == 1:
                    f+=1
                if g[r][c] == 2:
                    q.append([r,c])
        
        time = 0
        while q and f > 0:
            d = [0,1,0,-1,0]
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr,nc = r+d[i],c+d[i+1]
                    out = nr < 0 or nc < 0 or nr == m or nc == n
                    if out or g[nr][nc] != 1:
                        continue
                    g[nr][nc] = 2
                    q.append([nr,nc])
                    f-=1
            time+=1
        
        return time if f == 0 else -1