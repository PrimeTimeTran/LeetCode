class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def is_feasible(line):
            aAbove = 0.0
            aBelow = 0.0
            for sq in squares:
                x, y, l = sq
                total = l * l
                if line <= y:
                    aAbove += total
                elif line >= y + l:
                    aBelow += total
                else:
                    aboveHeight = (y + l) - line
                    belowHeight = line - y
                    aAbove += l * aboveHeight
                    aBelow += l * belowHeight
            return (aAbove - aBelow) > 0
        l, r = 0, 2*1e9
        for _ in range(60):
            m = (l + r) / 2.0
            if is_feasible(m):
                l = m
            else:
                r = m
        return r