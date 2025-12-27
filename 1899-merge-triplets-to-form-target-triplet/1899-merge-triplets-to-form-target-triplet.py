'''
1. Understand
Greedy.

5. Big O
Time:   O(n)
Space:  O(1)
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0
        for x in triplets:
            if x[0] <= target[0] and x[1] <= target[1] and x[2] <= target[2]:
                a, b, c = max(a, x[0]), max(b, x[1]), max(c, x[2])
        return [a,b,c] == target