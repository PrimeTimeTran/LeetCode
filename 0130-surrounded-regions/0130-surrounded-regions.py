'''
With nested loops transform perimeter island cells to T guarding for cycles. 
With nested loops transform O cells to X cells.
With nested loops transform T cells to O cells.
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
                perimeter = (r in [0, m-1] or c in [0, n-1])
                if board[r][c] == 'O' and perimeter:
                    capture(r,c)                   
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'