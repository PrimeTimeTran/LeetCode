'''
- Create graph using an adj list
- Understand a path a tree/graph
'''

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)       
        
        #  Build the graph
        for i, n in enumerate(parent):
            if i > 0:
                g[n].append(i)

        self.res = 0
        def dfs(i):
            cur = [0]
            for j in g[i]:
                c = dfs(j)
                if s[i] != s[j]:
                    cur.append(c)
            cur = nlargest(2, cur)
            self.res = max(self.res, sum(cur)+1)
            return max(cur)+1
        dfs(0)        
        return self.res