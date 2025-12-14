class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        if not g: return 0
        rank, parent, m, n = {}, {}, len(g), len(g[0])
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry: return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        for r in range(m):
            for c in range(n):
                if g[r][c] == "1":
                    parent[(r, c)] = (r,c)
                    rank[(r, c)] = 0
        for r in range(m):
            for c in range(n):
                if g[r][c] == "1":
                    for dr, dc in [(1,0), (0,1)]:
                        nr, nc = r + dr, c + dc
                        inbounds = 0 <= nr < m and 0 <= nc < n
                        if inbounds and g[nr][nc] == "1":
                            union((r, c), (nr, nc))
        return len({find(x) for x in parent})
