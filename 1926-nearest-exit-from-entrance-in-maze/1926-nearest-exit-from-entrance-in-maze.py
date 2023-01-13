class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        steps = 0
        DIR = [0,-1,0,1,0]
        q = deque([entrance])
        seen = set(entrance)
        m,n = len(maze), len(maze[0])
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (0 in [r, c] or r == m-1 or c == n-1) and [r, c] != entrance:
                    return steps
                for i in range(4):
                    nr,nc = r+DIR[i],c+DIR[i+1]
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        q.append([nr,nc])
            steps+=1
        return -1