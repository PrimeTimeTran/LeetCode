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
    def letterCombinations(self, digits: str) -> List[str]:
        store = {
            '2':"abc", '3':"def", '4':"ghi", '5':"jkl", 
            '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"
        }
        res = ['']
        for d in digits:
            res = [prefix + c for prefix in res for c in store[d]]

        return res