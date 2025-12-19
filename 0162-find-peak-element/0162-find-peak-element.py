'''
5-162-find-peak-element.py
l = 0, r = 3
(l+r)//2 = 1        # mid leans left
l + (r-l+1)//2 = 2  # mid leans right
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m-1] > nums[m]:
                r = m - 1
            else:
                l = m
        return l