'''
1. Understand
Greedy.

2. Diagram

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 
[    ]
   [           ]
                     [     ]
                                               [           ]
5. BigO
Time:   O(nlogn)
Space:  O(n)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals:
            prev = res[-1]
            if prev[1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(prev[1], end)
        return res
        # intervals.sort()
        # res = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     cur = intervals[i]
        #     prev = res[-1]
        #     if prev[1] < cur[0]:
        #         res.append(cur)
        #     else:
        #         res[-1][1] = max(cur[1], prev[1])
        # return res