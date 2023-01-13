class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        seen = set()
        def dfs(n, cur):
            if n == len(graph)-1:
                res.append(cur+[n])
            for nei in graph[n]:
                dfs(nei, cur + [n])
                    
        dfs(0,[])
        return res
            