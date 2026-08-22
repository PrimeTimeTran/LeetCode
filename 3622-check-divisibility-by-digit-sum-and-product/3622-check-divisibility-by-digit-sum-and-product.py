class Solution:
    def checkDivisibility(self, n: int) -> bool:
        vals = [int(v) for v in str(n)]
        total_sum = sum(vals)
        
        product = 1
        for v in vals:
            product *= v
            
        return n % (total_sum + product) == 0