class Solution:
    def solve(self, b: List[List[str]]) -> None:
        m,n = len(b), len(b[0])
        seen = set()
        def dfs(r,c):
            out = r < 0 or c < 0 or r == m or c == n or (r,c) in seen 
            if out or b[r][c] == 'X':
                return
            seen.add((r,c))
            b[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'O' and (r in [0, m-1] or c in [0, n - 1]):
                    dfs(r,c)
                    
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'O':
                    b[r][c] = 'X'
                    
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'T':
                    b[r][c] = 'O'