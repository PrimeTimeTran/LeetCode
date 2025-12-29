'''
1. Understand
Greedy.
5. Big O

Time:   O(nlogn + n) where n is the length of points
Space:  O(1) for two pointers
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        c, cur = 1, points[0][1]
        for start, end in points:
            if cur < start:
                c+=1
                cur = end
            else:
                cur = min(end, cur)
        return c