class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g, prob = defaultdict(list), defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append(v)
            g[v].append(u)
            prob[u, v] = prob[v, u] = succProb[i]

        h = [(-1, start)]
        seen = set()
        while h: 
            p, n = heappop(h)
            if n == end: return -p
            seen.add(n)
            for nn in g.get(n, []):
                if nn in seen: continue 
                heappush(h, (p * prob.get((n, nn), 0), nn))
        return 0
