class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rank, parent, R, C = {}, {}, len(grid), len(grid[0])
        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    parent[(r, c)] = (r, c)
                    rank[(r, c)] = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        inbounds = 0 <= nr < R and 0 <= nc < C
                        if inbounds and grid[nr][nc] == "1":
                            union((r, c), (nr, nc))
        roots = set(find(x) for x in parent)
        return len(roots)
