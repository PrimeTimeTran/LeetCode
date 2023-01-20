class Solution:
    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        return not target > j1 + j2 and target % gcd(j1, j2) == 0
