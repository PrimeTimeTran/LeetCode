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
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def back(rem, strings):
            if not rem:
                res.append(strings)
            for i in range(1, len(rem)+1):
                if rem[:i] == rem[:i][::-1]:
                    back(rem[i:], strings+[rem[:i]])
        back(s, [])
        return res