class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.end = len(graph)-1
        def dfs(n, path):
            if n == self.end:
                self.res.append(path+[n])
            
            for nei in graph[n]:
                dfs(nei, path+[n])
            
        dfs(0, [])
        
        return self.res