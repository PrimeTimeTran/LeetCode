'''
1. Constraints
Given a list of words and return a string the alien alphabet.

2. Diagram

t > f
w > e > r

3. Pseudocode
Create G using char of words. 
Identify most significant differing character and append word's to it. Guard for longer word first between two words with common prefix.

Perform Top sort using seen hashmap.

4. Code
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {c: [] for w in words for c in w}
        
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minlength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return ""
            for j in range(minlength):
                if w1[j] != w2[j]:
                    g[w1[j]].append(w2[j])
                    break
        res, seen = [], {}
        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = False
            for nei in g[c]:
                if not dfs(nei): return False
            seen[c] = True
            res.append(c)
            return True
        for c in g:
            if not dfs(c): return ""
            
        return "".join(res[::-1])