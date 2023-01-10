class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         prices = [inf]*n
#         prices[src] = 0
        
#         for i in range(k+1):
#             tmpPrices = prices.copy()
            
#             for s,d,p in flights:
#                 if prices[s] == inf:
#                     continue
#                 if prices[s]+p < tmpPrices[d]:
#                     tmpPrices[d] = prices[s] + p
#             prices = tmpPrices
        
#         return -1 if prices[dst] == inf else prices[dst]
    
        g = defaultdict(list)
        
        for u,v,w in flights:
            g[u].append((v,w))
            
        q = [[0, src, k+1]]
        seen = {}
        
        while q:
            cost,u,stops = heapq.heappop(q)
            if u == dst: return cost
            if u in seen and seen[u] >= stops : continue
            seen[u] = stops - 1
            if stops: 
                for v, w in g[u]:
                    heapq.heappush(q, (cost+w, v, stops-1))
        return -1