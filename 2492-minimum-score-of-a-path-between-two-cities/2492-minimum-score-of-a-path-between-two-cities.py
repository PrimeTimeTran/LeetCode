'''
DFS
DFS from 1 node finding the smallest score/distance road in any path connected to 1 node.
'''
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for u,v,w in roads:
            g[u].append((v,w)); g[v].append((u,w))
        
        q = deque([1])
        seen = set()
        res = inf
        while q:
            u = q.popleft()
            if u in seen: continue
            seen.add(u)
            for v, d in g[u]:
                res = min(res, d)
                q.append(v)
        return res