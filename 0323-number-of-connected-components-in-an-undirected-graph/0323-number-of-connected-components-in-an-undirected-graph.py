class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # g = {i:[] for i in range(n)}
        # for a,b in edges:
        #     g[a].append(b)
        #     g[b].append(a)
        # def dfs(n):
        #     if n in seen:
        #         return
        #     seen.add(n)
        #     for nei in g[n]:
        #         dfs(nei)
        # res = 0
        # seen = set()
        # for n in range(n):
        #     if n not in seen:
        #         dfs(n)
        #         res += 1
        # return res
    
        parent = list(range(n))
        
        # def find(p):
        #     while p != parent[p]:
        #         parent[p] = parent[parent[p]]
        #         p = parent[p]
        #     return p
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry 
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})