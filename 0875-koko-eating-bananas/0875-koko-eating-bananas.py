class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        while l + 1 < r:
            m = (l+r) // 2
            if sum(ceil(p/m) for p in piles) > h:
                l = m
            else:
                r = m
        return 