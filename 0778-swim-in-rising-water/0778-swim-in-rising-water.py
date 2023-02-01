class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         def valid(i, j):
#             return 0 <= i < m and 0 <= j < n
        
#         def get_neis(i, j):
#             return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        
#         heap = []
#         heapq.heappush(heap, (grid[0][0], 0, 0))
#         seen = {(0, 0): grid[0][0]}
#         while len(heap):
#             val, i, j = heapq.heappop(heap)
#             if i == m-1 and j == n-1:
#                 return val
#             for x, y in get_neis(i, j):
#                 if valid(x, y) and max(grid[x][y], val) < seen.get((x,y), float('inf')):
#                     seen[(x,y)] = max(grid[x][y], val)
#                     heapq.heappush(heap, (seen[(x,y)], x, y))
                    
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))