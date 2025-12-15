class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = cur = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                cur += 1
            else:
                cur = 1
            res += cur

        return res
