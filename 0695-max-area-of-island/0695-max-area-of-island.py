class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        m,n = len(g), len(g[0])
        seen = set()
        def dfs(r,c):
            o = r < 0 or c < 0 or r == m or c == n
            if o or (r,c) in seen or g[r][c] == 0:
                return 0
            seen.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        res = 0
        for r in range(m):
            for c in range(n):
                if g[r][c] and (r,c) not in seen:
                    res = max(res, dfs(r,c))
        return res