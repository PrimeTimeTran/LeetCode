class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))

        q = deque([1])
        
        seen = set()
        res = inf
        while q:
            n = q.popleft()
            for nei, d in g[n]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
                res = min(res, d)
                    
        return res