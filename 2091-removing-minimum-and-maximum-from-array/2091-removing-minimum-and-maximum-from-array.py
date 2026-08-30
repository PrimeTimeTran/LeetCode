class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum, maximum = min(nums), max(nums)

        a = nums.index(minimum)
        b = nums.index(maximum)

        l, r = min(a, b), max(a, b)
        n = len(nums)

        return min(
            r + 1,          # both from left
            n - l,          # both from right
            l + 1 + n - r   # min from left, max from right
        )