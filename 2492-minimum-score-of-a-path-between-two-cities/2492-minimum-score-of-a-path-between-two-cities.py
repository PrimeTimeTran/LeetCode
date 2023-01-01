class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(dict)
        for a,b,d in roads:
            g[a][b] = g[b][a] = d
            
        q = deque([1])
        res = float('inf')
        seen = set()
        while q:
            cur = q.popleft()
            for des, d in g[cur].items():
                if not des in seen:
                    seen.add(des)
                    q.append(des)
                res = min(res, d)
        
        return res
        