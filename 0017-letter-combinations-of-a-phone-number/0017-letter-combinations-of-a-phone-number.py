class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
            '8':"tuv", '9':"wxyz"}
        comb = [''] if digits else []
        for d in digits:
            comb = [p+char for p in comb for char in dict[d]]
        return comb