'''
Dijkstra
Create graph with flights and BFS with PQ. Check for cycles and update res on each item.

'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in flights:
            g[u].append((v, w))
            
        # price, src, steps remeaning
        pq, seen = [(0, src, k + 1)],  {}
        while pq: 
            price, u, s = heapq.heappop(pq)
            if u == dst:
                return price
            if u in seen and seen[u] >= s: continue
            seen[u] = s
            
            if s:
                for v, w in g[u]:
                    heapq.heappush(pq, [price+w, v, s-1])
        return -1
                    
        