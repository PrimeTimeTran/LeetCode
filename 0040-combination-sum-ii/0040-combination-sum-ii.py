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
    def combinationSum2(self, C: List[int], T: int) -> List[List[int]]:
        res = []
        C.sort()
        def back(rem, path):
            if sum(path) == T:
                return res.append(path)
            if sum(path) > T:
                return
            for i in range(len(rem)):
                if i > 0 and rem[i] == rem[i-1]:
                    continue
                back(rem[i+1:], path+[rem[i]])
        back(C, [])
        return res