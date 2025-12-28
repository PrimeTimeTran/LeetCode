'''
Create G and BFS on PQ with cost, city, num of remaining stops.
Guard cycle using a hashmap which contains number of stops remaining.
If the number of stops in the hashmap is greater than stops, continue; skipping this pq item's neighbors.

seen, q, g = {}, [[0,src,k+1]], defaultdict(list)
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g, q, seen = defaultdict(list), [[0,src,k+1]], {}
        for u,v,w in flights: g[u].append([v,w])
        while q:
            accum_cost, u, stops = heappop(q)
            if u == dst: return accum_cost
            if u in seen and seen[u] >= stops: continue
            seen[u] = stops - 1
            if stops:
                for des, cost in g[u]:
                    heappush(q, [cost + accum_cost, des, seen[u]])
        return -1