class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        
        while l<=r:
            n = nums[l] + nums[r]
            if n == target:
                return [l+1,r+1]
            elif n > target:
                r -= 1
            else:
                l += 1
            