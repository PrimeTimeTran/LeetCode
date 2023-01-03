class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out:
                return 0
            if (r,c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            DIR = [0, 1, 0, -1, 0]
            res = 1
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                res += dfs(nr,nc)
            return res

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    res = max(res, dfs(r,c))
        return res


