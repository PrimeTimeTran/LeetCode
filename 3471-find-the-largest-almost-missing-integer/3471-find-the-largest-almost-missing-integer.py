class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = Counter()
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]
            for num in set(subarray):
                counts[num] += 1
        unique = [num for num, count in counts.items() if count == 1]
        return max(unique) if unique else -1