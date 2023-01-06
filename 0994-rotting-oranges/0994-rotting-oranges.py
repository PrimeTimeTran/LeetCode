class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        d = [0,1,0,-1,0]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = d[i] + r, d[i+1] + c
                    out = nr < 0 or nc < 0 or nr == m or nc == n
                    if out or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
