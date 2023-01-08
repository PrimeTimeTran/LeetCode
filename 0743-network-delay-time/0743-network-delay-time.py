'''
Use BFS to implement dikjstra's algorithm.
Take the shortest path possible first from each node working through neighbors watching for cycles.

'''

from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append([v,w])
        seen = set()
        q = [[0,k]]
        while q:
            t, u = heappop(q)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heappush(q, [t+nt, v])
            
        
        return t if len(seen) == n else -1