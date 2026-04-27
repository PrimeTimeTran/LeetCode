from collections import deque

class Solution:
    def hasValidPath(self, grid):
        M, N = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        while q:
            x, y = q.popleft()
            if (x, y) == (M-1, N-1):
                return True
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited:
                    for rdx, rdy in dirs[grid[nx][ny]]:
                        if nx + rdx == x and ny + rdy == y:
                            visited.add((nx, ny))
                            q.append((nx, ny))
        return False