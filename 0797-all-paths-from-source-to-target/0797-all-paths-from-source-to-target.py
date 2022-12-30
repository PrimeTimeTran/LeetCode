class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph) - 1
        
        def dfs(n, path, res):
            if n == end:
                res.append(path+[n])
                return 
            for nei in graph[n]:
                dfs(nei, path+[n], res)
        dfs(0, [], res)
        return res
        