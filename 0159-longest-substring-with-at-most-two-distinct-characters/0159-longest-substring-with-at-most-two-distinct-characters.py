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
        w = {}
        for r, c in enumerate(s):
            w[c] = w.get(c, 0) + 1
            while len(w.keys()) > 2:
                w[s[l]] -=1
                if w[s[l]] == 0: del w[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res