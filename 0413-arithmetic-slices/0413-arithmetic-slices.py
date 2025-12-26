class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        @lru_cache(None)
        def f(i):
            if i < 2:
                return 0
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                return f(i-1) + 1
            return 0

        return sum(f(i) for i in range(n))

# class Solution:
#     def numberOfArithmeticSlices(self, nums):
#         n = len(nums)
#         if n < 3: return 0
#         dp = [0] * n
#         total = 0
#         for i in range(2, n):
#             if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
#                 dp[i] = dp[i-1] + 1
#                 total += dp[i]
#         return total


# class Solution:
#     def numberOfArithmeticSlices(self, nums):
#         total = 0
#         curr = 0

#         for i in range(2, len(nums)):
#             if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
#                 curr += 1
#                 total += curr
#             else:
#                 curr = 0

#         return total
