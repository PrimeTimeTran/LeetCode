class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for c in s: 
            ans = [x + cc for x in ans for cc in {c, c.swapcase()}]
        return ans 