'''
For each character of the string create a lower & uppercase set.
For both items, combine them with candidate res you have so far(extending it).
Return the result from doing this with all chars of the string.
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            res = [x + cc for x in res for cc in {c, c.swapcase()}]
        return res