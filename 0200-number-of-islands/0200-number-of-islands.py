def neighbors(R, C, r, c, directions=[(1,0),(-1,0),(0,1),(0,-1)]):
    return ((r+dr, c+dc) for dr, dc in directions if 0 <= r+dr < R and 0 <= c+dc < C)

class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        R, C = len(g), len(g[0])
        self.res, seen = 0, set()
        def dfs(r,c):
            if (r,c) in seen: return
            if not g[r][c] == "1": return
            seen.add((r, c))
            for dr, dc in neighbors(R, C, r, c):
                dfs(dr, dc)
        for r in range(R):
            for c in range(C):
                if g[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c)
                    self.res += 1
        return self.res