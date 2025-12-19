'''
1. Understand
Key mental insight
- In a rotated sorted array, the minimum element is the only element where the previous element is greater than it (or equivalently, it’s the “pivot point”).
- Another way to think: the minimum is always in the unsorted half of the current search range.

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]