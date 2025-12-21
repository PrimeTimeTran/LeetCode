class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            elif nums[l] == nums[m]:
                l += 1
                continue
            # If true, we know that left is completed sorted.
            elif nums[l] <= nums[m]:
                # ✅ Left Partition sorted but does target fall inside it?
                # If it does, then we can discard the rest of the search space.
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # If not, then it's inside the unsorted partition
                else: 
                    l = m + 1
            else:
                # ✅ Right Partition sorted but does target fall inside it?
                # If it does, then we can discard the rest of the search space.
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # If not, then it's inside the unsorted partition
                else: 
                    r = m - 1
        return False