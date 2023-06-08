class Solution:
    def countNegatives(self, grid):
        return sum(n<0 for r in grid for n in r)