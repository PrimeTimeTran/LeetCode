class Solution:
    def closedIsland(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and g[r][c] == 0:
                g[r][c] = 1
                dfs(r, c + 1)
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                edge = r == 0 or c == 0 or r == m - 1 or c == n - 1
                land = g[r][c] == 0
                if edge and land:
                    dfs(r, c)
        res = 0
        for r in range(m):
            for c in range(n):
                if g[r][c] == 0:
                    dfs(r, c)
                    res += 1
        return res
