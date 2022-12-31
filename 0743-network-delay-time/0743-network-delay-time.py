class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # seen, t = set(), 0
        # g = collections.defaultdict(list)
        # for u, v, w in times:
        #     g[u].append((v, w))
        # heap = [(0, k)]
        # while heap:
        #     t, u = heapq.heappop(heap)
        #     if u in seen: continue
        #     seen.add(u)
        #     if len(seen) == n: break
        #     for v, nt in g[u]:
        #         heapq.heappush(heap, (t+nt, v))
        # return t if len(seen)==n else -1
        
        seen, t = set(), 0
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v,w))
            
        heap = [(0, k)]
        
        while heap:
            t, u = heapq.heappop(heap)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heapq.heappush(heap, (t+nt, v))
            
        return t if len(seen) == n else -1