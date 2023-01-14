'''
DFS 
DFS twice with post and pre order traversal.
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

        def dfs(root, pre):
            for i in g[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        
        def dfs2(root, pre):
            for i in g[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        print(count,res)
        return res