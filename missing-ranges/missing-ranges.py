class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        final = []
        start = lower
        for i in range(len(nums)):
            if lower <= nums[i] <= upper:
                if start < nums[i]:
                    final.append([start, nums[i] - 1])
                start = nums[i]+1

        if start <= upper:
            final.append([start, upper])
        return final