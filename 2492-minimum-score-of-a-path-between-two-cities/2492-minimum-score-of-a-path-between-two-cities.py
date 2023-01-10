class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
            
        seen, q = set(), deque([1])
        res = inf
        while q:
            u = q.popleft()
            if u in seen: continue
            seen.add(u)
            for v, w in g[u]:
                if v not in seen:
                    q.append(v)
                res = min(res, w)
                
        return res
            