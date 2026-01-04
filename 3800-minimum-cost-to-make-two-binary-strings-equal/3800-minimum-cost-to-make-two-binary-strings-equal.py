class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        c = [0, 0]
        for a, b in zip(s, t):
            if a != b:
                c[int(a)] += 1
        c0, c1 = c
        res1 = (c0 + c1) * flipCost
        res2 = min(c0, c1) * swapCost + abs(c0 - c1) * flipCost
        res3 = min(c0, c1) * swapCost + abs(c0 - c1) // 2 * (swapCost + crossCost) +  abs(c0 - c1) % 2 * flipCost
        return min(res1, res2, res3)