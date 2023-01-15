'''
Sliding window, grow while window is valid. Shrink when window invalid.

'ec'
w {
    e: 1
    c: e 
}

'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, l = 0, 0
        seen = set()
        win = {}
        for r, c in enumerate(s):
            win[c] = win.get(c, 0) + 1
            while len(list(set(s[l:r+1]))) > 2:
                l+=1
                cur = s[l:r+1]
            res = max(res, r-l+1)
        return res