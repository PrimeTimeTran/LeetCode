class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, r, c = heappop(pq)
            res = max(res, T)
            if r == c == N - 1:
                return res
            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heappush(pq, (grid[nr][nc], nr, nc))