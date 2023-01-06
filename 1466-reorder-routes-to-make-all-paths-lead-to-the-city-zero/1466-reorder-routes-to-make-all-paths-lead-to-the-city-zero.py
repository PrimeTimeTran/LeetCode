class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        seen = set()
        edges = {(a, b) for a, b in connections}
        neighbors = defaultdict(list)

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(c):
            for n in neighbors[c]:
                if n in seen:
                    continue
                if (n, c) not in edges:
                    self.res += 1
                seen.add(n)
                dfs(n)

        seen.add(0)
        dfs(0)
        return self.res
