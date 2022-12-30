class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        end = len(graph) - 1
        res = []
        def dfs(n, p, res):
            if n == end:
                res.append(p)
            for nei in graph[n]:
                dfs(nei, p+[nei], res)
        dfs(0, [0], res)
        return res