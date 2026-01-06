class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dp(a, b):
            if a == b: return True
            if Counter(a) != Counter(b): return False
            for i in range(1, len(a)):
                no_swap_match = dp(a[:i], b[:i]) and dp(a[i:],  b[i:])
                swap_match = dp(a[:i], b[-i:]) and dp(a[i:],  b[:-i])
                if no_swap_match or swap_match:
                    return True
            return False
        return dp(s1, s2)