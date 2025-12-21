class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            # M must be greater than l otherwise we'd enter an infinite loop.
            m = (l+r+1) // 2
            # ✅ We know that there exists at least 1 peak left of 
            # the current index/midpoint so we can discard the right half.
            if nums[m-1] > nums[m]:
                r = m - 1
            else:
                # 🔑 l does not move if l == m
                # This line is why our algorithm for m is different.
                l = m
        return l
