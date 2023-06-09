class Solution:
    def isMajorityElement(self, nums, target):
        k = len(nums) // 2
        if nums[k] != target:
            return False
        lo = bisect.bisect_left(nums, target, 0, k)
        hi = lo + k
        return hi < len(nums) and nums[hi] == target