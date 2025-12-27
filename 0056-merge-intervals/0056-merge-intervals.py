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
            cur_end = res[-1][1]
            if cur_end < start:
                res.append([start, end])
            else:
                res[-1][1] = max(cur_end, end)
        return res
