class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for i, n in enumerate(nums):
            r-=n
            if l == r: return i
            l+=n
        return -1
            