class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in roads:
            g[a].append(b);g[b].append(a)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                val = len(g[i]) + len(g[j]) - (j in g[i])
                ans = max(ans, val)
        return ans