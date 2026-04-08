class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[r] <= nums[m]:
                if nums[r] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums)-1
#         while l <= r:
#             m = (l+r) // 2
#             if nums[m] == target:
#                 return m
#             elif nums[l] <= nums[m]:                # The left partition is sorted
#                 if nums[l] <= target < nums[m]:     # Does the target lie in the sorted half?
#                     r = m - 1
#                 else:
#                     l = m + 1
#             else:
#                 if nums[m] < target <= nums[r]:
#                     l = m + 1
#                 else:
#                     r = m - 1
#         return -1