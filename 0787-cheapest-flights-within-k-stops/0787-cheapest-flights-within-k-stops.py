from heapq import heappop, heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0
        
        for _ in range(k+1):
            tmp = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == inf: continue
                
                if prices[s]+p < tmp[d]:
                    tmp[d] = prices[s]+p
            
            
            prices = tmp
            
        return -1 if prices[dst] == inf else prices[dst]