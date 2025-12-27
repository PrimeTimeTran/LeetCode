class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen, t, n, q = set(), 0, len(grid), [[grid[0][0], 0, 0]]
        while q:
            elevation, r, c = heappop(q)
            if (r,c) in seen: continue
            seen.add((r,c))
            t = max(t, elevation)
            if r == c == n-1:
                return t
            for dr, dc in [r+1, c], [r-1, c], [r,c+1], [r,c-1]:
                inbounds = 0 <= dr < n and 0 <= dc < n
                if inbounds:
                    heappush(q, [grid[dr][dc], dr, dc])