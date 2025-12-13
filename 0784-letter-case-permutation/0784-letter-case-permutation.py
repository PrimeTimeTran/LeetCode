'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            res = [x + cc for x in res for cc in {c, c.swapcase()}]
        return res