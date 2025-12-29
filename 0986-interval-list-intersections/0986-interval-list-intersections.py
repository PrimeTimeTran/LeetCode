'''
1. Understand
Two-pointer sweep over two sorted interval lists.

At each step, compare one interval from each list:
- Compute their intersection, if it exists
- Move forward the pointer of the interval that ends first,
  since it cannot overlap with any future interval.

This efficiently exhausts both lists while collecting all intersections.

5. Big O
Time:   O(n + m)
Space:  O(1) extra (excluding output)
'''
class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            start = max(l1[i][0], l2[j][0])
            end = min(l1[i][1], l2[j][1])
            if start <= end:
                res.append([start, end])
            if l1[i][1] < l2[j][1]:
                i+=1
            else:
                j+=1
        return res