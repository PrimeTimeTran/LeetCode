class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans, seen = 0, set()
        R, C = len(grid), len(grid[0])
        def dfs(r,c):
            inbounds = 0 <= r < R and 0 <= c < C and (r,c) not in seen
            if inbounds and grid[r][c] == "1":
                seen.add((r,c)) 
                for dr, dc in [r+1,c],[r-1,c],[r,c+1],[r,c-1]:
                    dfs(dr, dc)
                return True
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and dfs(r,c):
                    self.ans+=1
        return self.ans