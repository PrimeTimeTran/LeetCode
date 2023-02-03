class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        seen = set()
        def dfs(r,c):
            inbounds = 0 <= r < m and 0 <= c < n
            if inbounds and g[r][c] and (r,c) not in seen:
                seen.add((r,c))
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0

        res = 0
        for r in range(m):
            for c in range(n):
                if g[r][c]:
                    res = max(res, dfs(r,c))
        return res