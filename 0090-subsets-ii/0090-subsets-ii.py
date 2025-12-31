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
        def back(cur, path, res = []):
            res.append(path)
            for i in range(len(cur)):
                if i > 0 and cur[i] == cur[i-1]: continue
                back(cur[i+1:], path+[cur[i]])
            return res
        return back(sorted(nums), [])