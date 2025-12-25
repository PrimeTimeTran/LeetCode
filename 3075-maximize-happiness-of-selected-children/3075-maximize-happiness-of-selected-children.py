class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res, n = [], 0
        happiness.sort(reverse=True)
        for i, h in enumerate(happiness):
            if i < k:
                res.append(h - n if h - n > 0 else 0)
                n+=1
        return sum(res)