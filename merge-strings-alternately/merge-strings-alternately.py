class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))

        a1, a2 = [c for c in w1], [c for c in w2]
        res = []
        while a1 or a2:
            if a1:
                res.append(a1.pop(0))
            if a2:
                res.append(a2.pop(0))
        
        return ''.join(res)
        