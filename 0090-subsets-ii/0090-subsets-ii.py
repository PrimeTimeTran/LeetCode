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
        nums.sort()
        res = []
        def dp(cur, path):
            res.append(path)
            for i in range(len(cur)):
                if i > 0 and cur[i] == cur[i-1]: continue
                dp(cur[i+1:], path+[cur[i]])
        dp(nums, [])
        return res
