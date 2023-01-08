'''
BFS G using PQ. Push time forward from each node. Guard for cycles and if seen node matches n, break.
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v,w))
            
        pq, seen = [[0,k]], set()
        
        while pq:
            time, u = heapq.heappop(pq)
            # time, u = pq.pop()
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: return time
            for v, nt in g[u]:
                heapq.heappush(pq, [time+nt, v])
                # pq.append([time+nt, v])
        return -1
        return time if len(seen) == n else -1