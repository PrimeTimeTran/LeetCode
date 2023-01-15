class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g= defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append((v,succProb[i]))
            g[v].append((u,succProb[i]))

        h = [(-1, start)]
        seen = set()
        while h: 
            p, n = heappop(h)
            if n == end: return -p
            seen.add(n)
            for nn, w in g[n]:
                if nn in seen: continue 
                heappush(h, (p * w, nn))
        return 0
