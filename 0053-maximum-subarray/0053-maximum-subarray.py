'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = nums[0], 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            ans = max(ans, cur)
        return ans


