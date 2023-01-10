class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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