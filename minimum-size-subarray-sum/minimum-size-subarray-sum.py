from sys import maxsize

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = maxsize
        left, total = 0, 0
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1
        
        return res if res != maxsize else 0