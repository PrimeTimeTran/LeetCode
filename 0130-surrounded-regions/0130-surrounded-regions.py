'''
Iterate mat DFSing on border O cells. In DFS change O cell and neighbor O cells to T
Iterate mat and turn all O cell to X.
Iterate mat and turn all T cell to O.
'''

class Solution:
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(b), len(b[0])
        
        seen = set()
        def dfs(r,c):
            o = r < 0 or c < 0 or r == m or c == n or (r,c) in seen
            if o or b[r][c] == 'X':
                return
            seen.add((r,c))
            b[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'O' and (r in [0, m-1] or c in [0, n-1]):
                    dfs(r,c)
        
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'O':
                    b[r][c] = 'X'
                    
        for r in range(m):
            for c in range(n):
                if b[r][c] == 'T':
                    b[r][c] = 'O'
                    