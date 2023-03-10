'''
Create G and BFS on PQ with cost, city, num of remaining stops.
Guard cycle using a hashmap which contains number of stops remaining.
If the number of stops in the hashmap is greater than stops, continue; skipping this pq item's neighbors.
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in flights:
            g[u].append((v,w))
            
        pq = [[0, src, k+1]]
        seen = {}
        while pq:
            c, u, stops = heappop(pq)
            if u == dst: return c
            
            if u in seen and seen[u] >= stops: continue
            seen[u] = stops-1
            
            if stops:
                for v, w in g[u]:
                    heappush(pq, (c+w, v, stops-1))
        return -1