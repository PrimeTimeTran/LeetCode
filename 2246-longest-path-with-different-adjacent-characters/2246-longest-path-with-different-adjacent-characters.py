class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        for i,j in enumerate(parent):
            if j >= 0:
                g[j].append(i)
        
        res = [0]
        def dfs(i):
            cur = [0]
            for j in g[i]:
                c = dfs(j)
                if s[i] != s[j]:
                    cur.append(c)
            cur = nlargest(2, cur)
            res[0] = max(res[0], sum(cur)+1)
            return max(cur)+1
            
        dfs(0)
        return res[0]