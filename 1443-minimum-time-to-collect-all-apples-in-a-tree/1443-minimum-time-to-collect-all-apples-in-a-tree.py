class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = set()

        def dfs(n):
            if n in seen:
                return 0
            seen.add(n)
            secs = 0
            for child in g[n]:
                secs += dfs(child)
            if secs > 0:
                return secs + 2
            return 2 if hasApple[n] else 0

        return max(dfs(0) - 2, 0)
