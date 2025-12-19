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
        def back(cur, path):
            if not cur:
                res.append(path)
            for i in range(len(cur)):
                back(cur[:i]+cur[i+1:], path+[cur[i]])                
            return res
        return back(nums, [])