class Solution:
    def pacificAtlantic(self, g: List[List[int]]) -> List[List[int]]:
        res, R, C = [], len(g), len(g[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for dr, dc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                inbounds = 0 <= dr < R and 0 <= dc < C
                if inbounds and g[dr][dc] >= g[r][c]:
                    dfs(dr, dc, ocean)

        for r in range(R):
            dfs(r, 0, pac)
            dfs(r, C-1, atl)
        for c in range(C):
            dfs(0, c, pac)
            dfs(R-1, c, atl)

        for r in range(R):
            for c in range(C):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
