class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        c = Counter(nums)
        for key, val in c.items():
            if val == n: return key