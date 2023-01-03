class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        go = itertools.permutations(nums, 3)
        res = 0
        for a,b,c in go:
            if a < b < c:
                res+=1
        return res