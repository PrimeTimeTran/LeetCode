class Solution:
    def trapRainWater(self, g: List[List[int]]) -> int:
        if not g or not g[0]: return 0
        q, level, res, m, n = [], 0, 0, len(g), len(g[0])
        if m < 3 or n < 3: return 0
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    heappush(q, [g[r][c], r, c])
                    g[r][c] = -1
        while q:
            height, r, c = heappop(q)
            level = max(level, height)
            for dr, dc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                inbounds = 0 <= dr < m and 0 <= dc < n
                if inbounds and g[dr][dc] != -1:
                    heappush(q, [g[dr][dc], dr, dc])
                    if g[dr][dc] < level:
                        res += level - g[dr][dc]
                    g[dr][dc] = -1
        return res
