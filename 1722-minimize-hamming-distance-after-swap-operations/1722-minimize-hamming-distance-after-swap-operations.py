from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        uf = UnionFind(n)
        
        # 1. Build components
        for a, b in allowedSwaps:
            uf.union(a, b)
        
        # 2. Group indices by component
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)
        
        # 3. Count mismatches per component
        res = 0
        
        for indices in groups.values():
            count = Counter()
            
            # count source values
            for i in indices:
                count[source[i]] += 1
            
            # try to match target values
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1
        
        return res
        