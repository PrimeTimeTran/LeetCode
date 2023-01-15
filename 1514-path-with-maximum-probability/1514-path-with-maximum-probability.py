class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g= defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append((v,succProb[i]))
            g[v].append((u,succProb[i]))

        h = [(-1, start)]
        seen = set()
        while h: 
            p, u = heappop(h)
            if u == end: return -p
            seen.add(u)
            for v, w in g[u]:
                if v in seen: continue 
                heappush(h, (p * w, v))
        return 0
