class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], pairs: List[List[str]]) -> bool:
        if len(s1) != len(s2): return False
        
        for w1, w2 in zip(s1,s2):
            if w1 == w2: continue
            val = any(w1 in pair and w2 in pair for pair in pairs)
            if not val: return False
        return True