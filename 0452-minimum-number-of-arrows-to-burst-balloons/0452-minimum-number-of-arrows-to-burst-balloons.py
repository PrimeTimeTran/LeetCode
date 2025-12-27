'''
1. Understand
Greedy.

5. Big O
Time:   O()
Space:  O()
'''
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         n, c = len(points), 1
#         if n == 0: return 0
#         points.sort(key = lambda x: x[1])
#         cur_end = points[0][1]
#         for p in points:
#             if cur_end < p[0]:
#                 c += 1
#                 cur_end = p[1]
#         return c
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        c, cur_end = 1, points[0][1]
        for p in points:
            if cur_end < p[0]:
                cur_end = p[1]
                c+=1
        return c