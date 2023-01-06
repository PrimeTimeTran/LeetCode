'''
With nested loops transform perimeter island cells to T. 
Next transform all O's to X's.
Transform T's back to X's
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def capture(r,c):
            out = r < 0 or c < 0 or r == m or c == n
            if out or board[r][c] != 'O':
                return
            board[r][c] = 'T'

            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r in [0, m-1] or c in [0, n-1]):
                    capture(r,c)                   
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'