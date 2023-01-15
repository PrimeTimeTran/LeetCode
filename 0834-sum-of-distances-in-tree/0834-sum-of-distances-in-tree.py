'''
DFS 
DFS twice with post and pre order traversal. Similar too graph valid tree in that we must send in -1 to guard cycles.
Create a count list which contains count of all nodes in subtree.
Create res whcih contains distance.
'''
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        res = [0] * N
        count = [1] * N
        for a, b in edges:
            g[a].append(b); g[b].append(a)

        def dfs(n, p):
            for i in g[n]:
                if i != p:
                    dfs(i, n)
                    count[n] += count[i]
                    res[n] += count[i] + res[i]
                    
        def dfs2(n, p):
            for i in g[n]:
                if i != p:
                    res[i] = res[n] -count[i] + N - count[i]
                    dfs2(i, n)
        dfs(0, -1)
        dfs2(0, -1)
        return res