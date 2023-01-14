class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)
        
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        seen = set()
        def dfs(n):
            secs = 0
            seen.add(n)
            for nei in g[n]:
                if nei not in seen:
                    secs += dfs(nei)
            if secs > 0:
                return secs + 2
            return 2 if hasApple[n] else 0
        
        return max(dfs(0) - 2, 0)