'''
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        seen = set()
        def dfs(n):
            for nei in g[n]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res
        