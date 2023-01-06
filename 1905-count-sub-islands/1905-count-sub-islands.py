class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        seen = set()
        m, n = len(grid1), len(grid1[0])

        def dfs(r, c):
            out = (
                r < 0 or c < 0 or r == m or c == n or grid2[r][c] == 0 or (r, c) in seen
            )
            if out:
                return True
            seen.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False
            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            return res

        count = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c] and (r, c) not in seen and dfs(r, c):
                    count += 1
        return count
