class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        firstIndex = l
        if nums[l] != target: return [-1,-1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r+1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        secondIndex = l
        return [firstIndex, secondIndex]