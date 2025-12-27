'''
1. Understand
Greedy.

5. Big O
Time:   O()
Space:  O()
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        c, cur_end = 0, -inf
        for start, end in pairs:
            if start > cur_end:
                c+=1
                cur_end = end
        return c