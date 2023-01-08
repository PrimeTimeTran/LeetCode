class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in flights:
            g[u].append([v, w])

        pq, seen = [(0, src, k + 1)], dict()
        while pq:
            d, u, s = heapq.heappop(pq)
            if u == dst:
                return d

            if u in seen and seen[u] >= s: continue
            seen[u] = s

            if s:
                for v, w in g[u]:
                    heapq.heappush(pq, (d + w, v, s - 1))
        return -1

#         prices = [inf]*n
#         prices[src] = 0

#         for i in range(k+1):
#             tmpPrices = prices.copy()

#             for s, d, p in flights:
#                 if prices[s] == inf:
#                     continue
#                 if prices[s]+p < tmpPrices[d]:
#                     tmpPrices[d] = prices[s] + p
#             prices = tmpPrices

#         return -1 if prices[dst] == inf else prices[dst]


# Bellman Ford
# this time o(e*k), normally o(e*v)
