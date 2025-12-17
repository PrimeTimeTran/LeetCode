class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            zeros = n - ones
            res += ones * zeros

        return res