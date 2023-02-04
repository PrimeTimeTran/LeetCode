'''
Iterate matrix adding rotten oranges to Q and counting fresh oranges.
BFS Q +1 time each layer. Change fresh oranges to rotten, add them to q, and decrementing fresh count.
If at the end fresh is 0, return time, else -1
'''

class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        f,t = 0, 0
        q = deque([])
        for r in range(m):
            for c in range(n):
                if g[r][c] == 2:
                    q.append((r,c))
                elif g[r][c] == 1:
                    f+=1
        d = [0,-1,0,1,0]    
        seen = set()
        while q and f > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    nr,nc = r+d[i], c+d[i+1]
                    inbounds = 0 <= nr < m and 0 <= nc < n
                    if inbounds and (nr,nc) not in seen and g[nr][nc] == 1:
                        f-=1
                        g[nr][nc] = 2
                        seen.add((nr,nc))
                        q.append((nr,nc))
            
            t+=1
        return t if f == 0 else -1