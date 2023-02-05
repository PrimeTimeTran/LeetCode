class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l = 0
        for i, n in enumerate(nums):
            l+=n
            if l == sum(nums[i:]):
                return i
        return -1
            
