'''
1. Understand
Greedy.

5. Big O
Time:   O(nlogn)
Space:  O(1)
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        c, cur_end = 0, -inf
        for start, end in pairs:
            if cur_end < start:
                cur_end = end
                c+=1
        return c