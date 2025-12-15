class Solution:
    def maxArea(self, H: List[int]) -> int:
        ans, l, r = 0, 0, len(H) -1
        while l < r:
            ans = max(ans, (r - l) * min(H[r], H[l]))
            if H[l] < H[r]:
                l+=1
            else: 
                r-=1
        return ans