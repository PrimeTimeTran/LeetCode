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
    def combinationSum(self, C: List[int], T: int) -> List[List[int]]:
        res = []
        def back(i, path):
            if i == len(C) or sum(path) > T:
                return
            if sum(path) == T:
                res.append(path)
                return 
            back(i+1, path)
            back(i, path+[C[i]])
        back(0, [])
        return res