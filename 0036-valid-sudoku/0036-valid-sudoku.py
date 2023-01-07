class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        m,n = len(b), len(b[0])
        rowSets = defaultdict(set)
        colSets = defaultdict(set)
        squareSets = defaultdict(set)
        
        for r in range(m):
            for c in range(n):
                num = b[r][c]
                if num == '.':
                    continue
                if num in rowSets[r] or num in colSets[c] or num in squareSets[(r//3, c//3)]:
                    return False
                rowSets[r].add(num)
                colSets[c].add(num)
                squareSets[(r//3, c//3)].add(num)
        return True