class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur, ans = 0, 1
        for d in s:
            if int(d) > k: return -1
            cur = 10*cur + int(d)
            
            if cur > k:
                ans += 1
                cur = int(d)
        return ans
                