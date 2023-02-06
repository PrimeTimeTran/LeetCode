class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a, b = nums[:n], nums[n:]
        res = [n for tup in zip(a,b) for n in tup]
        return res
