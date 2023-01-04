class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = (10**9 + 7)
        
        @cache
        def modpow(b, e):
            return b ** e % MOD
        
        ct = Counter(nums[:k])
        cur = 0
        for v in ct:
            cur = (cur + modpow(v, ct[v])) % MOD
        ans = cur
        for i in range(1, n - k + 1):
            L, R = nums[i - 1], nums[i + k - 1]
            if L == R: continue
            cur -= modpow(L, ct[L])
            if ct[L] > 1:
                cur += modpow(L, ct[L] - 1)
            if ct[R]:
                cur -= modpow(R, ct[R])
            cur += modpow(R, ct[R] + 1)
            cur %= MOD
            ans = max(cur, ans)
            ct[L] -= 1
            ct[R] += 1
        return ans
    