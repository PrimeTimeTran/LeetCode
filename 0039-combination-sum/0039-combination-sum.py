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
            if len(C) == i or sum(path) > T:
                return
            if sum(path) == T:
                res.append(path)
                return
            back(i+1, path)
            back(i, path + [C[i]])
            return res
        return back(0, [])