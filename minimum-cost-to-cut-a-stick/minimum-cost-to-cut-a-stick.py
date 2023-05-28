class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])  # add 2 fake cuts as the boundary of the first cut
        cuts.sort()
        @functools.lru_cache(None)
        def f(i, j):
            if i + 1 >= j: return 0
            return cuts[j] - cuts[i] + min((f(i, k) + f(k, j) for k in range(i+1, j)), default=0)  # go through all the cuts as the first cut
        return f(0, len(cuts)-1)