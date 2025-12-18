'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        pDiag, nDiag, C = set(), set(), set()
        def back(r):
            if r == n:
                res.append([''.join(r) for r in board])
                return 
            for c in range(n):
                clear = not ((r+c) in pDiag or (r-c) in nDiag or c in C)
                if clear:
                    pDiag.add(r+c)
                    nDiag.add(r-c)
                    C.add(c)
                    board[r][c] = 'Q'
                    back(r+1)
                    pDiag.remove(r+c)
                    nDiag.remove(r-c)
                    C.remove(c)
                    board[r][c] = '.'
        back(0)
        return res