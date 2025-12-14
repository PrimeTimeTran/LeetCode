class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for n in nums:
            vals[n] = vals.get(n,0)+1
        # arr = sorted(vals, key=lambda v: (-vals[v], v))
        arr = sorted(vals, key = vals.get, reverse = True)

        return arr[:k]
