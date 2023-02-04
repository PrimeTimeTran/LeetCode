class Solution:
    def maxCount(self, banned: List[int], n: int, k: int) -> int:
        banned = set(banned)
        nums = [i for i in range(1, n+1) if i not in banned]
        nums = list(accumulate(map(int, nums)))
        add = 1 if k in nums else 0
        return bisect_left(nums, k) + add