class Solution:
    def canMeasureWater(self, j1: int, j2: int, targetCapacity: int) -> bool:
        return not targetCapacity > j1 + j2 and targetCapacity % gcd(j1, j2) == 0
