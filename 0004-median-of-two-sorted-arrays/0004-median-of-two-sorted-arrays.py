class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = heapq.merge(nums1,nums2)
        nums = list(nums)
        if len(nums) % 2 == 0:
            l = nums[len(nums) // 2 -1]
            r = nums[len(nums) // 2]
            return (l+r) / 2
        else:
            return nums[len(nums) // 2]