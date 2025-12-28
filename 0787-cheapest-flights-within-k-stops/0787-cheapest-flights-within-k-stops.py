'''
Create G and BFS on PQ with cost, city, num of remaining stops.
Guard cycle using a hashmap which contains number of stops remaining.
If the number of stops in the hashmap is greater than stops, continue; skipping this pq item's neighbors.

maxRemainingStops, q, g = {}, [[0,src,k+1]], defaultdict(list)
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g, q, min_stops = defaultdict(list), [[0, src, 0]], {}
        for u,v,w in flights: g[u].append([v,w])
        while q:
            accum_cost, u, accum_stops = heappop(q)
            if u == dst: return accum_cost
            if accum_stops >= k+1: continue
            if u in min_stops and min_stops[u] <= accum_stops: continue
            min_stops[u] = accum_stops + 1
            for des, cost in g[u]:
                heappush(q, [cost + accum_cost, des, min_stops[u]])
        return -1