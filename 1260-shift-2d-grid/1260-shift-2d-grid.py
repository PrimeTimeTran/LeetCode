class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [x for row in grid for x in row]
        k %= len(flat)
        flat = flat[-k:] + flat[:-k]
        return [
            flat[i:i + n]
            for i in range(0, len(flat), n)
        ]
    