class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in roads:
            g[u].add(v)
            g[v].add(u)
            
        
        ans = 0
        for i in range(n): 
            for j in range(i+1, n):
                val = len(g.get(i, set())) + len(g.get(j, set())) - (j in g.get(i, set()))
                ans = max(ans, val)
        return ans 