'''
BFS graph carrying time forward with a PQ. If number of seen nodes break loop and return last time.
Guard cycles with set

'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
            
        pq = [[0,k]]
        seen = set()
        while pq:
            t,u = heapq.heappop(pq)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heapq.heappush(pq, [nt+t, v])
        return t if len(seen) == n else -1
                