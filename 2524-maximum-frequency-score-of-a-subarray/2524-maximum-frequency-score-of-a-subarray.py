'''
Use sliding window of len k from left to right.
Use a counter to track distinct values and their powers.
Use cur and ans to track running totals to avoid TLE.

'''

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def powmod(b,e):
            return b**e % mod
        
        c = Counter(nums[:k])
        
        cur = 0
        for b,e in c.items():
            cur = (cur + powmod(b,e)) % mod
        ans = cur
        
        for i in range(1, len(nums)-k+1):
            L,R = nums[i-1], nums[i+k-1]
            if L == R: continue
            cur -= powmod(L, c[L])
            if c[L] > 1:
                cur += powmod(L, c[L] - 1)
            
            if c[R]:
                cur -= powmod(R, c[R])
            
            cur +=  powmod(R, c[R]+1)

            cur %= mod
            ans = max(ans, cur)
            
            c[L] -= 1
            c[R] += 1
                
        return ans