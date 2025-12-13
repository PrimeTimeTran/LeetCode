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
    def permute(self, nums):
        res = []
        def back(rem, path):
            if not rem:
                res.append(path)
            for i in range(len(rem)):
                back(rem[:i] + rem[i+1:], path+[rem[i]])
        back(nums, [])
        return res