'''
BFS rotten oranges to fresh oranges counting remaining fresh.
Return time if all fresh oranges become rotten.
'''

class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        f,q = 0, deque([])
        m,n = len(g), len(g[0])
        
        for r in range(m):
            for c in range(n):
                if g[r][c] == 2:
                    q.append([r,c])
                if g[r][c] == 1:
                    f +=1
        t = 0
        while q and f > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                d = [0,1,0,-1,0]
                for i in range(4):
                    nr,nc = d[i]+r, d[i+1]+c
                    out = nr < 0 or nc < 0 or nr == m or nc == n or g[nr][nc] != 1
                    if out:
                        continue
                    g[nr][nc] = 2
                    f -= 1
                    q.append([nr,nc])
            t+=1
        return t if f == 0 else -1
        