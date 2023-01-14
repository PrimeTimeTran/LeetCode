class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        for i, n in enumerate(parent):
            g[n].append(i)
        
        self.res = 0
        def dfs(n):
            cur = [0]
            for i in g[n]:
                c = dfs(i)
                if s[i] != s[n]:
                    cur.append(c)
            cur = nlargest(2,cur)
            self.res = max(self.res, sum(cur)+1)
            return max(cur)+1
        
        
        dfs(0)
        return self.res
        