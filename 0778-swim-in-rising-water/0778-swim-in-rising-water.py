'''
1. Understand
"The first time a node is removed from the heap, its cost is final."

5. Big O
Time:   O()
Space:  O()
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen, t, n, q = set(), 0, len(grid), [[grid[0][0], 0, 0]]
        while q:
            elevation, r, c = heappop(q)
            seen.add((r,c))
            t = max(t, elevation)
            if r == c == n-1:
                return t
            for dr, dc in [r+1, c], [r-1, c], [r,c+1], [r,c-1]:
                inbounds = 0 <= dr < n and 0 <= dc < n
                unseen = (dr, dc) not in seen
                if inbounds and unseen:
                    heappush(q, [grid[dr][dc], dr, dc])