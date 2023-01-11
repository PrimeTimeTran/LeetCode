class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level-1
    
        n, res = len(grid), 0
        land = {(i, j) for i, j in product(range(n), range(n)) if grid[i][j]}
        water = {(i, j) for i, j in product(range(n), range(n)) if not grid[i][j]}
        while water:
            if not land: return -1
            land = {(x, y) for i, j in land for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if (x, y) in water}
            water -= land
            res += 1
        return res or -1