class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        cnt = Counter(p)
        
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[l]] += 1
                l += 1
            if r - l + 1 == len(p):
                return True
            
        return False