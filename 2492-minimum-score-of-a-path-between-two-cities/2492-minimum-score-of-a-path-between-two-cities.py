class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(dict)
        
        for a,b,d in roads:
            g[a][b] = g[b][a] = d
            
        dq = deque([1])
        visit = set()
        res = float('inf')
        while dq:
            cur = dq.popleft()
            for des, d in g[cur].items():
                if des not in visit:
                    visit.add(des)
                    dq.append(des)
                res = min(res, d)
        return res