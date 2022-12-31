'''
1. Constraints 
We're given a 2d array, and should return a 2d array which consists of paths from 0 to n-1

2. Diagram

0 -> 1 -> 3
[0]
    [0, 1]
          [0, 1, 3]

0 -> 2 -> 3
[0]


2. 



'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.end = len(graph)-1
        def dfs(n,path):
            if self.end == n:
                self.res.append(path+[n])
            for nei in graph[n]:
                dfs(nei, path+[n])
        dfs(0, [])
        return self.res