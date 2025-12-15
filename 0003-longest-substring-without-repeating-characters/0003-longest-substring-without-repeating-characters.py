'''
Sliding Window:
Loop chars of string adding char to seen.
Before adding, check if the char is in seen. If so, remove s[l] from the set and increment l by 1.
Each iteration update ans to max of ans & r - l + 1
Return ans
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans, seen = 0, 0, set()
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l+=1
            seen.add(c)
            ans = max(ans, r-l+1)
        return ans