# https://leetcode.com/problems/subsets-ii
'''

'''
class Solution:
    def combinationSum2(self, C: List[int], T: int) -> List[List[int]]:
        res = []
        C.sort()
        def back(cur, path):
            if sum(path) > T:
                return
            if sum(path) == T:
                res.append(path)
                return
            for i in range(len(cur)):
                if i > 0 and cur[i] == cur[i-1]:
                    continue
                back(cur[i+1:], path + [cur[i]])
        back(C, [])
        return res
