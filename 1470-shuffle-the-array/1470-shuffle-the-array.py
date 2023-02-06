class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a, b = nums[:n], nums[n:]
        res = []
        res.extend([[x,y]for x,y in zip(a,b)])
        merged = list(itertools.chain(*res))
        return merged
