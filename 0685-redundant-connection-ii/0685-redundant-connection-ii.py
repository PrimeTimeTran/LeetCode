class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)  # Track parents to detect two parents
        cand1 = cand2 = None

        # Step 1: check for node with two parents
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                # v has two parents
                cand1 = [parent[v], v]  # first edge
                cand2 = [u, v]          # second edge
                break

        # Union-Find setup
        uf = list(range(n + 1))
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            uf[py] = px
            return True

        # Step 2: iterate edges to detect cycle
        for u, v in edges:
            if [u,v] == cand2:  # skip second candidate edge if exists
                continue
            if not union(u,v):
                if cand1:
                    return cand1
                return [u,v]

        return cand2
