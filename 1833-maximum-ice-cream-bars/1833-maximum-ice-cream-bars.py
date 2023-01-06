class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        for cost in sorted(costs):
            if coins - cost >= 0:
                res +=1
            coins -= cost
        return res