'''
1. Understand
We want to converge our pointers toward:
1) The index where a number is strictly less and closest to the target.
2) The index where a number is strictly more and closest to the target.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        firstIndex = l
        if nums[firstIndex] != target: return [-1, -1]
        l, r = 0, len(nums)-1
        while l < r:
            m = l + ((r-l+1) // 2)
            if nums[m] > target:
                r = m - 1
            else:
                l = m
            m = (l+r) // 2
        lastIndex = r
        return [firstIndex, lastIndex]

