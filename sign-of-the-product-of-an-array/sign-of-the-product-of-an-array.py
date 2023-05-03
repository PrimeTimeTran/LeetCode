class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for n in nums:
            val *= n

        if val > 0: return 1
        if val < 0: return -1
        return 0
