# 1. Constraints
# Receive one 2d array which represents a matrix/grid. 
# 1 = land
# 2 = water

# 2. Diagram
# 

# 3. Pseudocode
# - Loop rows/cols and traverse cell if it is land.
# - For land cells expand in 4 directions
# - If the expansion is water or out of bounds, increment perimeter count.
# - Otherwise continue expanding

# 4. Code

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.count = 0
        seen = set()
        def traverse(r,c):
            if (r,c) in seen: return
            out = r < 0 or r == R or c < 0 or c == C
            if out or grid[r][c] == 0:
                self.count += 1
                return 
            seen.add((r,c))
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    traverse(r, c)

        return self.count