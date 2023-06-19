class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(max(list(accumulate(gain))), 0)