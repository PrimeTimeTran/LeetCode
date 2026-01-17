class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0 # the rectange side
        coordinats = list(zip(bottomLeft, topRight))
        
        for ((ax1, ay1), (ax2, ay2)), ((bx1, by1), (bx2, by2)) in combinations(coordinats, 2):
            overlapX = min(ax2, bx2) - max(ax1, bx1)
            overlapY = min(ay2, by2) - max(ay1, by1)

            if overlapX > 0 and overlapY > 0:
                minSquareSide = min(overlapX, overlapY)
                res = max(res, minSquareSide)

        return res * res