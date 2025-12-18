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
            if sum(path) == n and len(path) == k:
                return res.append(path)
            if sum(path) > n or len(path) > k:
                return
            for i in range(start, 10):
                back(i+1, path+[i])
        back(1, [])
        return res