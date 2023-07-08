class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        q=sorted([weights[i]+weights[i+1] for i in range(len(weights)-1)])
        return sum(q[-k+1:]) - sum(q[:k-1])    