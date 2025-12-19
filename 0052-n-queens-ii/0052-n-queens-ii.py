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
    def totalNQueens(self, n: int) -> int:
        res, board = [], [['.']*n for _ in range(n)]
        C, pDiag, nDiag = set(), set(), set()
        def back(r):
            if r == n:
                res.append([''.join(r) for r in board])
            for c in range(n):
                clear = not (c in C or r+c in pDiag or r-c in nDiag)
                if clear: 
                    pDiag.add((r+c))
                    nDiag.add((r-c))
                    C.add(c)
                    board[r][c] = 'Q'
                    back(r+1)
                    pDiag.remove((r+c))
                    nDiag.remove((r-c))
                    C.remove(c)
                    board[r][c] = '.'
            return res
        return len(back(0))