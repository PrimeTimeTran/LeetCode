class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        for i,j in enumerate(parent):
            if j >= 0:
                g[j].append(i)
        
        res = [0]
        def dfs(i):
            candi = [0]
            for j in g[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    candi.append(cur)
                    
            candi = nlargest(2, candi)
            res[0] = max(res[0], sum(candi) + 1)
            return max(candi) + 1
        
        dfs(0)
        return res[0]