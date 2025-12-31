# class Solution:
#     def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
#         res, board = 0, [[0] * n for _ in range(m)]
#         def dfs(r, c):
#             if r == m-1: return True
#             reached = False
#             for dr, dc in [[r+1,c], [r-1,c], [r,c+1],[r,c-1]]:
#                 inbounds = 0 <= dr < m and 0 <= dc < n
#                 if inbounds and board[dr][dc] == 0:
#                     tmp = board[dr][dc]
#                     board[dr][dc] = '.'
#                     reached = reached or dfs(dr, dc)
#                     board[dr][dc] = tmp
#             return reached
#         for i, cur in enumerate(cells):
#             for c in range(n):
#                 if board[0][c] == 0 and dfs(0, c):
#                     res = max(res, i)
#             board[cur[0]-1][cur[1]-1] = 1
#         return res
class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        def can_cross(day):
            board = [[0]*n for _ in range(m)]
            for i in range(day):
                r, c = cells[i]
                board[r-1][c-1] = 1

            def dfs(r, c):
                if r == m - 1: return True
                board[r][c] = 1
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 0:
                        if dfs(nr, nc):
                            return True
                return False
            for c in range(n):
                if board[0][c] == 0 and dfs(0, c):
                    return True
            return False
        l, r = 0, len(cells)
        while l < r:
            mid = (l + r + 1) // 2
            if can_cross(mid):
                l = mid
            else:
                r = mid - 1
        return l