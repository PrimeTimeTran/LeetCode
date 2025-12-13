'''
1. Understand
We want to return a list of lists. The nested lists should be of length k and contain numbers in the range 1 - n.

2. Diagram
3. Pseudocode
4. Code
5. BigO
Time: O()
Space: O()
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(start, path):
            if len(path) == k:
                return res.append(path[:])
            for i in range(start, n+1):
                path.append(i)
                back(i+1, path)
                path.pop()
        back(1, [])
        return res