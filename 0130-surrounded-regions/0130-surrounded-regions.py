class Solution:
    def solve(self, b: List[List[str]]) -> None:
        R, C, seen = len(b), len(b[0]), set()
        def explore(r,c):
            explored = (r,c) in seen
            inbounds = 0 <= r < R and 0 <= c < C
            if not inbounds or explored or b[r][c] == 'X': return
            seen.add((r,c))
            b[r][c] = 'T'
            for dr,dc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                explore(dr,dc)
        for r in range(R):
            for c in range(C):
                if b[r][c] == 'O' and (r in [0, R-1] or c in [0, C-1]):
                    explore(r,c)
        for r in range(R):
            for c in range(C):
                if b[r][c] == 'O':
                    b[r][c] = 'X'
        for r in range(R):
            for c in range(C):
                if b[r][c] == 'T':
                    b[r][c] = 'O'