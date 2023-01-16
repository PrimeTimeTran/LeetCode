'''
Create G and BFS with PQ on maximized probability and node.
Begin with -1 to find max probability as we add to PQ with multiplication. 
Guard cycles using set.
'''

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for i, (u,v) in zip(succProb, edges):
            g[u].append((v,i)); g[v].append((u,i))
            
        pq = [[-1,start]]
        seen = set()
        while pq:
            p, u = heappop(pq)
            if u == end: return -p
            seen.add(u)
            for v, w in g[u]:
                if v in seen: continue
                heappush(pq, ((p*w), v))    
        return 0