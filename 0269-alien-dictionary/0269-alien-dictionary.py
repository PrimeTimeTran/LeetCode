'''
Create a graph using chars of word.
Guard for long matching prefix words appearing before shorter.
Find first diff char of w1 and w2. Add w2 to g of w1
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {c: [] for w in words for c in w}
        # g = defaultdict(list)
        
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minlength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return ''
            for j in range(minlength):
                if w1[j] != w2[j]:
                    g[w1[j]].append(w2[j])
                    break
        res = []
        seen = {}
        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = False
            for n in g[c]:
                if not dfs(n): return False
            seen[c] = True
            res.append(c)
            return True
        
        
        
        for c in g:
            if not dfs(c): return ""
        return "".join(res[::-1])