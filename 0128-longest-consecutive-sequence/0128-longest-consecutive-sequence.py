class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in nums:
            if n-1 not in seen:
                cur = 0
                while cur+n in seen:
                    cur+=1
                res = max(res, cur)
        return res