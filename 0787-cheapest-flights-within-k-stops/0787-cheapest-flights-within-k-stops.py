'''
BFS G with PQ with cost, src, stops. 
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in flights:
            g[u].append([v,w])
            
        pq = [[0, src, k+1]]
        seen = {}
        
        while pq:
            cost, u, stops = heapq.heappop(pq)
            if u == dst: return cost
            
            if u in seen and seen[u] >= stops: continue
            seen[u] = stops
            
            if stops:
                for v, w in g[u]:
                    heapq.heappush(pq, [cost+w, v, stops-1])
        return -1
                
                