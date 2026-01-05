class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        while l < r:
            m = (l+r) // 2
            if sum(ceil(p/m) for p in piles) <= h:
                r = m
            else:
                l = m + 1
        return l