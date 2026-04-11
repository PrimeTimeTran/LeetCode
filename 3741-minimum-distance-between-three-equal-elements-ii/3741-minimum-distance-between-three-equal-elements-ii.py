# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         cur = inf
#         length = len(nums)
#         for i in range(length):
#             for j in range(i+1, length):
#                 for k in range(j+1, length):
#                     if nums[i] == nums[j] == nums[k]:
#                         x = abs(i - j) + abs(j-k) + abs(k-i)
#                         if x < cur:
#                             cur = x
#         return cur if cur != inf else -1
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        res = float('inf')
        for indices in pos.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i+2] - indices[i])
                res = min(res, dist)

        return res if res != float('inf') else -1