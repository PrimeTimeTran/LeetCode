# 1. Understand
# Check that each row, column and block has unique numbers. If they do it's solvable otherwise it's not.
# 2. Diagram
# Iterate the matrix and add to a seen set for rows, cols and blocks. If the number has already been seen in that container return false
# 3. Pseudocode
# 4. Code
# 5. Analyze
# O(M*N) where M * N are the lengths of the rows and columns respectively
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C, B = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.': continue
                key = (r//3, c//3)
                seen = num in R[r] or num in C[c] or num in B[key]
                if seen: return False
                R[r].add(num)
                C[c].add(num)
                B[key].add(num)
        return True