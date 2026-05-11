class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            cur = list(str(n))
            for c in cur:
                res.append(int(c))
        return res