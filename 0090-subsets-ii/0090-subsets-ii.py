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
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def back(rem, path):
            res.append(path)
            for i in range(len(rem)):
                if i > 0 and rem[i] == rem[i-1]:
                    continue
                back(rem[i+1:], path+[rem[i]])
        back(nums, [])
        return res