class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        def get_neis(i, j):
            return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = {(0, 0): grid[0][0]}
        while len(heap):
            val, i, j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return val
            for x, y in get_neis(i, j):
                if is_valid(x, y) and max(grid[x][y], val) < visited.get((x,y), float('inf')):
                    visited[(x,y)] = max(grid[x][y], val)
                    heapq.heappush(heap, (visited[(x,y)], x, y))