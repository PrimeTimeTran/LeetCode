class Solution:
    def largestVariance(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0)+1
        perms = itertools.permutations(chars, 2)
        def kadane(a,b):
            count = res = 0
            isA = isB = False
            aCount = chars[a]
            bCount = chars[b]
            for c in s:
                if not a == c and not b == c: continue
                if count < 0 and aCount != 0 and bCount != 0:
                    isA = isB = False
                    count = 0
                if c == a:
                    aCount -=1
                    count += 1
                    isA = True
                if c == b:
                    bCount -=1
                    count -= 1
                    isB = True
                if isA and isB:    
                    res = max(res, count)           
            return res
        res = 0
        for a,b in perms:
            res = max(res, kadane(a, b))
        return res