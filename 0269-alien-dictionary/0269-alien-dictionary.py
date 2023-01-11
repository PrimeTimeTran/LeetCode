'''
1.
Given a list of words and should return a string if valid lexicographicallyy sorted string can be found.

2.

t > f 
w > e > r

3.
- Create adj list using chars of words.
- Iterate thru pairs of words finding greatest largest difference.
- Using G perform a topilogical sort and return reversed version.


4.


'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {c: [] for w in words for c in w}
        
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
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
        
        
        return ''.join(res[::-1])