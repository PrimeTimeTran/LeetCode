'''
g = defaultdict(list)
        
for a, b in edges:
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
        res += 1
return res
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(x,y):
            nx, ny = find(x), find(y)
            if nx != ny:
                p[ny] = nx
        for x, y in edges:
            union(x,y)
            
        return len({find(x) for x in range(n)})