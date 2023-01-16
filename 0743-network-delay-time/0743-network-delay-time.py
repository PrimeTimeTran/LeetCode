'''
Create G and BFS with vertex and times. PQ items hold accumulated time and node.
When num of seen node matches n return time. Else return -1
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
            
        pq = [[0,k]]
        seen = set()
        while pq:
            t, u = heappop(pq)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: return t
            for v, w in g[u]:
                heappush(pq, (t+w, v))
        return -1