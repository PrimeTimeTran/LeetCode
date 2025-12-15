class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        R, C, B = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = b[r][c]
                if num == '.': continue
                key = (r//3, c//3)
                seen = num in R[r] or num in C[c] or num in B[key]
                if seen: return False
                R[r].add(num)
                C[c].add(num)
                B[key].add(num)
        return True