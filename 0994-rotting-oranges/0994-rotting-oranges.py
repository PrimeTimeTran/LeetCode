'''
Iterate matrix adding rotten oranges to Q and counting fresh oranges.
BFS Q +1 time each layer. Change fresh oranges to rotten, add them to q, and decrementing fresh count.
If at the end fresh is 0, return time, else -1
'''

class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        f,q = 0, deque([])
        m,n = len(g), len(g[0])
        for r in range(m):
            for c in range(n):
                if g[r][c] == 2:
                    q.append((r,c))
                elif g[r][c] == 1:
                    f+=1
        res = 0 
        d = [0,-1,0,1,0]
        while q and f > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    nr,nc = r+d[i],c+d[i+1]
                    o = nr < 0 or nc < 0 or nr == m or nc == n
                    if o or g[nr][nc] != 1:
                        continue
                    g[nr][nc] = 2
                    q.append((nr,nc))
                    f -= 1
            res+=1
        print(f)
        return res if f == 0 else-1