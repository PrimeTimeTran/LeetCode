class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        seen, g = set(), defaultdict(list)
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))
        n, q = len(edges), [(passingFees[0], 0, 0)]
        min_time = [float('inf')] * n
        while q:
            accum_fee, origin, accum_time = heappop(q)
            if accum_time > maxTime: continue
            if origin == len(passingFees) - 1:
                return accum_fee
            if accum_time >= min_time[origin]:
                continue
            min_time[origin] = accum_time
            for destination, t in g[origin]:
                heapq.heappush(q, (accum_fee + passingFees[destination], destination, accum_time + t))
        return -1