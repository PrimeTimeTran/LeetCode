class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        
        DIR = [0,-1,0,1,0]
        q = deque([entrance])
        steps = 0
        seen = set(entrance)
        while q:
            for _ in range(len(q)):
                xo, yo = q.popleft()
                if (0 in [xo, yo] or xo == m-1 or yo == n-1) and [xo, yo] != entrance:
                    return steps
                for i in range(4):
                    x,y = xo+DIR[i],yo+DIR[i+1]
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == '.' and (x,y) not in seen:
                        seen.add((x,y))
                        q.append([x,y])
            steps+=1
        return -1