class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0 
        pq = [[grid[0][0], 0, 0]]
        seen = set((0,0))
        while pq:
            V, r, c = heappop(pq)
            res = max(res, V)
            if r == c == n-1: return res
            for nr, nc in [[r+1,c],[r,c+1], [r-1,c], [r,c-1]]:
                if (nr,nc) not in seen and (0 <= nr < n and 0 <= nc < n):
                    seen.add((nr,nc))
                    heappush(pq, [grid[nr][nc], nr, nc])