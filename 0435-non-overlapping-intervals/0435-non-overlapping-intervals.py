'''
1. Understand
Greedy.

2. Diagram

1  2  3  4  5
[  ]
   [  ]
      [  ]
[     ]
5. Big O
Time:   O(nlogn)
Space:  O(1)
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur_end, c = -inf, 0
        for start, end in intervals:
            if cur_end <= start:
                cur_end = end
            else:
                c+=1
                cur_end = min(cur_end, end)
        return c