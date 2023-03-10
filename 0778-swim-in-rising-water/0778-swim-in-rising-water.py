'''
BFS
BFS with PQ on value of cell/row/column. On each cell update res to max of current res and value.
Flow 4 cardinal directions to unseen inbound cells and add them to PQ and seen set.
'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0 
        n = len(grid)
        seen = set((0,0))
        pq = [[grid[0][0], 0, 0]]
        while pq:
            V, r, c = heappop(pq)
            res = max(res, V)
            if r == c == n-1: return res
            for nr, nc in [[r+1,c],[r,c+1], [r-1,c], [r,c-1]]:
                inbounds = 0 <= nr < n and 0 <= nc < n
                unseen = (nr,nc) not in seen
                if inbounds and unseen:
                    seen.add((nr,nc))
                    heappush(pq, [grid[nr][nc], nr, nc])