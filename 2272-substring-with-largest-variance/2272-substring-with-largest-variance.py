class Solution:
    def largestVariance(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c,0)+1
        perms = itertools.permutations(chars, 2)

        def kadane(a,b):
            res = count = 0
            aCount = chars[a]
            bCount = chars[b]
            isA = isB = False
            for c in s:
                if not c == a and not c == b: continue
                if count < 0 and aCount != 0 and bCount != 0:
                    isA = isB = False
                    count = 0
                if c == a:
                    aCount-=1
                    isA = True
                    count += 1
                if c == b:
                    bCount -=1
                    isB = True
                    count-=1
                if isA and isB:
                    res = max(res, count)
            return res
        res = 0
        for a,b in set(perms): 
            res = max(res, kadane(a,b))
        return res