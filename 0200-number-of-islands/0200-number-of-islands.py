class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] < self.size[pv]:  # Merge pu to pv
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        
        component = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0": continue
                component += 1
                curId = r * n + c
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    neiId = nr * n + nc
                    if uf.union(curId, neiId):
                        component -= 1
        return component