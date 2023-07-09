'''
1. Constraints.
We take 1 string. We return 1 int.

2.

aababbb
3
babbb


3. Pseudocode
Kadane's Algorithm

a = 1
b = -1
[1, 1, -1, 1, -1, -1, -1]
2

a = -1
b = 1
[-1,-1, 1,-1,1,1,1]
3

- Identify permutations of 2 characters
- Iterate through each permutation and identifying maximum subarray
- Return res


4.


'aaabbb'
0


            res, maxCount = 0, 0
            aCount = chars[a]
            bCount = chars[b]
            isA = isB = False
            for c in s:
                if not c == a and not c == b: continue
                if maxCount < 0 and aCount != 0 and bCount != 0:
                    isA = isB = False
                    maxCount = 0
                if c == a:
                    aCount -=1
                    maxCount +=1
                    isA = True
                if c == b:
                    bCount -=1
                    maxCount -=1
                    isB = True
                if isA and isB:
                    res = max(res, maxCount)
            return res
        for a,b in set(perms):
            print('hi')
            res = max(res, kadane(a,b))
        return res

'''
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