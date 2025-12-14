'''
1. Understand

2. Diagram

3. Pseudocode

4. Code

5. Big O
Time = 
Space = 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = postfix = 1
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n 
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res