'''
BFS G with PQ with acc cost, src, stops.
Check if u is destination and return cost if true. If we cross k, continue; updating seen of vertix with new stops value.
Add neighbrs to PQ if k not yet crossed.

'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in flights:
            g[u].append((v,w))
        
        # acc, src, moves
        pq = [[0,src,k+1]]
        seen = {}
        while pq:
            cost, u, moves = heapq.heappop(pq)
            if u == dst: return cost
            if u in seen and seen[u] >= moves: continue
            seen[u] = moves - 1
            if moves:
                for v, w in g[u]:
                    heapq.heappush(pq, [cost+w, v,moves-1])
        return -1