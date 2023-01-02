class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        
        for u,v,t in times:
            g[u].append((v,t))
            
        seen = set()
        q = [(0,k)]
        
        while q:
            t, u = heapq.heappop(q)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heapq.heappush(q,(nt+t, v))
        
        return t if len(seen) == n else -1