class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = heapq.merge(nums1, nums2)
        nums = list(nums)
        m = len(nums) // 2
        if len(nums) % 2 == 0:
            l = nums[m-1]
            r = nums[m]
            return (l + r) / 2
        else:
            return nums[m]