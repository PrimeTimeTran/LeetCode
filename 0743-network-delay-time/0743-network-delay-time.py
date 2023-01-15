'''
Create G and BFS with vertex and times. Create Q and append prev node and accumulated time thus far.
Use set to identify nm of seen nodes and break if found. Use heapq to go shortest time first, Dikjstra
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
            
        q = [[0,k]]
        seen = set()
        
        while q:
            t, u = heappop(q)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: return t
            for v, w in g[u]:
                heappush(q, (w+t, v))
        
        return -1