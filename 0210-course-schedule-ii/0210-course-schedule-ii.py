class Solution:
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in P:
            g[a].append(b)
        
        self.res, seen = [], {}
        
        def can_complete(n):
            if n in seen: return seen[n]
            seen[n] = False
            for pre in g[n]:
                if not can_complete(pre): return False
            seen[n] = True
            self.res.append(n)
            return seen[n]
        
        for c in range(N):
            if not can_complete(c):
                return []
        return self.res