class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            g[i].add(j)
            g[j].add(i)

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
        return res