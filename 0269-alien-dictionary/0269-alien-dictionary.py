'''
1. Constraints
Given a list of words and return a string the alien alphabet.

2. Diagram

t > f
w > e > r

3. Pseudocode
Create G using chars of words and word pairs.
Find most significant differing char and append post char to it. 
Guard for longer word first in word pair with common prefix.
Perform top sort using seen hashmap.
Return joined reversed topsort.
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {c:[] for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
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
        print(g, res)
        return "".join(res[::-1])