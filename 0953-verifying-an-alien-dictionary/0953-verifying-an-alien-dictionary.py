'''
1. Constraints
Receive list of words and string reprensenting the alphabet
Return a boolean

2. Diagram



3. Pseudocode
Create g of key letter and value index from order


'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        g = {}
        for i, c in enumerate(order):
            g[c] = i
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if g[w1[j]] > g[w2[j]]: return False
                    break
        return True