class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        seen = [[False] * n for _ in range(m)]
        diagonals = [0] * (m + n - 1)
        q = deque()
        q.append((0, 0))
        while q:
            i, j = q.popleft()
            if grid[i][j] == 0 or seen[i][j]:
                continue
            seen[i][j] = True
            diagonals[i + j] += 1
            if i:
                q.append((i - 1, j))
            if j:
                q.append((i, j - 1))
            if i < m - 1:
                q.append((i + 1, j))
            if j < n - 1:
                q.append((i, j + 1))
        return any([x < 2 for x in diagonals[1:-1]])