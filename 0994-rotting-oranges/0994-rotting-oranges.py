'''
Use nested loops to count number of fresh oranges and add any rotten orange to q.
While q and number of fresh > 0, process each q item.
When processing adj cells check for out of bounds and not fresh orange, 1. If so continue.
Change this new cell to be rotten, append it to the q, decrement fresh.

Add to time after each for loop of queue.
Return time if fresh is 0 else return -1

'''
class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        q, f = deque([]), 0
        
        m, n = len(g), len(g[0])
        for r in range(m):
            for c in range(n):
                if g[r][c] == 2:
                    q.append([r,c])
                if g[r][c] == 1:
                    f +=1
        t = 0
        d = [0,1,0,-1,0]
        while q and f > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = d[i]+r,d[i+1]+c
                    
                    out = nr < 0 or nc < 0 or nr == m or nc == n
                    
                    if out or g[nr][nc] != 1:
                        continue
                    f -= 1
                    g[nr][nc] = 2
                    q.append([nr,nc])
            t+=1
        return t if f == 0 else -1