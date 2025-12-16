class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        for i in range(len(nums)+1):
            res ^= i
        return res