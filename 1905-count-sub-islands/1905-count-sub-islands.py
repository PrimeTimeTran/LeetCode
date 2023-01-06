'''
Loop cells and DFS on unseen land in grid2.
In DFS return true if out of bounds, cell of grid 2 is water, or cell has been seen. 
By default res is truue, but if grid1 of cell is water, set to false; recurse but still flag as invalid.
'''
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1), len(grid1[0])
        
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n or grid2[r][c] == 0 or (r,c) in seen
            if out:
                return True
            
            seen.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False
            res = dfs(r+1,c) and res
            res = dfs(r-1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res
            return res
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c] and (r,c) not in seen and dfs(r,c):
                    res +=1
        return res