# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         n, m = len(nums1), len(nums2)
        
#         dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
#         for i in range(n):
#             for j in range(m):
#                 prod = nums1[i] * nums2[j]
#                 dp[i][j] = max(
#                     prod,
#                     prod + max(0, dp[i-1][j-1]) if i > 0 and j > 0 else prod,
#                     dp[i-1][j] if i > 0 else float('-inf'),
#                     dp[i][j-1] if j > 0 else float('-inf')
#                 )
#         return dp[n-1][m-1]
from functools import lru_cache
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            # Option 1: pair current elements
            take = nums1[i] * nums2[j] + max(0, dfs(i + 1, j + 1))
            # Option 2 & 3: skip one element
            skip1 = dfs(i + 1, j)
            skip2 = dfs(i, j + 1)
            return max(take, skip1, skip2)
        return dfs(0, 0)