class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
                
        for k, v in a.items():
            if abs(b[k] - v) > 3:
                return False
            
        for k, v in b.items():
            if abs(a[k] - v) > 3:
                return False
        return True