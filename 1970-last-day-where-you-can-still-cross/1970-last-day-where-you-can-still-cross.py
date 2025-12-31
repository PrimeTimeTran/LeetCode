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
                    inbounds = 0 <= nr < m and 0 <= nc < n
                    if inbounds and board[nr][nc] == 0:
                        if dfs(nr, nc): return True
            for c in range(n):
                if board[0][c] == 0 and dfs(0, c): return True
            return False
        
        l, r = 0, len(cells)
        while l < r:
            mid = (l + r + 1) // 2
            if can_cross(mid):
                l = mid
            else:
                r = mid - 1
        return l