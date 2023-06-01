class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @cache
        def fn(i, k):
            """Return probability of obtaining k heads from coins[i:]."""
            if k < 0: return 0 
            if i == len(prob): return k == 0
            return prob[i]*fn(i+1, k-1) + (1-prob[i])*fn(i+1, k)
        
        return fn(0, target)