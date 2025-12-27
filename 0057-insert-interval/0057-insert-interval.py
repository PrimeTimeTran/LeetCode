'''
1. Understand
Greedy.

We iterate through the sorted intervals and compare each interval
with the new interval `n`.

At every step:
- If `n` is completely before the current interval, we can insert `n`
  and return immediately.
- If the current interval is completely before `n`, we keep it.
- Otherwise, the intervals overlap, so we merge them into `n`.

2. Diagram

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

1  2  3  4  5  6  7  8  9
[     ]
         [     ]
   [        ]

3. Big O

Time:   O(n)
Space:  O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], n: List[int]) -> List[List[int]]:
        res = []
        for i, cur in enumerate(intervals):
            if n[1] < cur[0]:
                res.append(n)
                return res + intervals[i:]
            elif n[0] > cur[1]:
                res.append(cur)
            else:
                n = [min(cur[0], n[0]), max(cur[1], n[1])]
        res.append(n)
        return res