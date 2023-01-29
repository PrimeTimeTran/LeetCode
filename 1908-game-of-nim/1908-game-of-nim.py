class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        mask = 0
        for i, x in enumerate(piles): mask |= x << 3*i
        
        @cache
        def fn(mask): 
            """Return True if current player can win by playing optimally."""
            for i in range(len(piles)): 
                val = (mask >> 3*i) & 7
                for k in range(1, val+1): 
                    mask0 = mask - (k << 3*i)
                    if not fn(mask0): return True 
            return False 
        
        return fn(mask)