class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        
        par = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}
        
        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return 1
        
        def similar(s, d):
            return sum(i != j for i, j in zip(s, d)) in {0, 2}
        
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    union(i, j)
        
        return sum(i == find(i) for i in range(n))