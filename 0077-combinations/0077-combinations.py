'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(start, path):
            if len(path) == k:
                return res.append(path)
            if len(path) > k:
                return
            for i in range(start, n+1):
                back(i+1, path+[i])
        back(1, [])
        return res
