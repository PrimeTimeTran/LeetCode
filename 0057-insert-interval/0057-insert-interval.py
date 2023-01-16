'''
1. Constraints
Input list of lists and new interval/list. Return output list of lists.

2. Diagram



3. Pseudocode
Loop through intervals comparing current start > previous end.


4. Code



'''
class Solution:
    def insert(self, intervals: List[List[int]], n: List[int]) -> List[List[int]]:
        res = []
        for i, cur in enumerate(intervals):
            if n[1] < cur[0]:
                res.append(n)
                return res + intervals[i:]
            elif cur[1] < n[0]:
                res.append(cur)
            else:
                n = [min(n[0], cur[0]), max(n[1], cur[1])]
        res.append(n)
        return res