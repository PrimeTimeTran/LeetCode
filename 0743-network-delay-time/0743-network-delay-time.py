class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v,w))
        
        seen, pq = set(), [[0,k]]
        while pq:
            t, u = heapq.heappop(pq)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: return t
            for v, w in g[u]:
                heapq.heappush(pq, (t+w, v))
        return -1