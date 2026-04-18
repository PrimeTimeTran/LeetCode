class Solution:
    def mirrorDistance(self, n: int) -> int:
        chars = str(n)[::-1]
        return abs(n - int(chars))