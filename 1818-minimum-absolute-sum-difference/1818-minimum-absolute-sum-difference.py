from bisect import bisect_left
from typing import List

MOD = 10**9 + 7

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(nums1)
        total = 0
        best_gain = 0
        for a, b in zip(nums1, nums2):
            curr = abs(a - b)
            total += curr
            # find closest value in nums1 to b
            i = bisect_left(sorted_nums1, b)
            if i < len(sorted_nums1):
                best_gain = max(best_gain, curr - abs(sorted_nums1[i] - b))
            if i > 0:
                best_gain = max(best_gain, curr - abs(sorted_nums1[i-1] - b))
        return (total - best_gain) % MOD