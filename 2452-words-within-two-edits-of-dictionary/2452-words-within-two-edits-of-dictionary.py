'''
1. Understand
Given two lists that both contain strings create a list of words from the queries arr 
that match words in the dict arr when the word is edited 2 or less times

2. Diagram
3. Pseudocode
4. Code.
5. Big O
'''

def within_two_edits(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            if diff > 2:
                return False
    return True

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for w in dictionary:
                if within_two_edits(q, w):
                    ans.append(q)
                    break
        return ans