'''
Create a undirected acyclic graph as "happy case".
Traverse happy case graph and if it isn't found in "reality" graph set, increment res.
'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        seen = set()
        self.res = 0
        roads = {(a, b) for a, b in connections}
        def dfs(c):
            for n in neighbors[c]:
                if n in seen:
                    continue
                if (n, c) not in roads:
                    self.res += 1
                seen.add(n)
                dfs(n)

        seen.add(0)
        dfs(0)
        return self.res
