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
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def back(start, path):
            if len(path) > k or sum(path) > n: return
            if len(path) == k and sum(path) == n:
                return res.append(path)
            for i in range(start, 10):
                back(i+1, path+[i])
        back(1, [])
        return res