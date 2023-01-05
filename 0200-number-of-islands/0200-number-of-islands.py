'''

Iterate cells using nested loops. 
Use DFS to mark each land cell as seen. 
Guard against out of bounds and explore outwards n,e,s,w recursively.
Increment res when land found and return res at the end.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out:
                return
            if (r,c) in seen or grid[r][c] == '0':
                return
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
            
        
        res = 0
        for r in range(m):
            for c in range(n):
                if dfs(r,c) and grid[r][c] == '1':
                    
                    res+=1
                    
        return res