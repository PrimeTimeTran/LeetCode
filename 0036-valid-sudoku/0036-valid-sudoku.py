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
        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.': continue
                key = (r//3, c//3)
                seen = num in rows[r] or num in cols[c] or num in blocks[key]
                if seen: return False
                rows[r].add(num)
                cols[c].add(num)
                blocks[key].add(num)
        return True