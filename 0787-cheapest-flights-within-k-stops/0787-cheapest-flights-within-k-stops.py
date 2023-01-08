class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf]*n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == inf:
                    continue
                if prices[s]+p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == inf else prices[dst]


# Bellman Ford
# this time o(e*k), normally o(e*v)
