class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(n):
            if not n: return None
            if n in seen: return seen[n]
            seen[n] = Node(n.val)
            for nei in n.neighbors:
                seen[n].neighbors.append(dfs(nei))
            return seen[n]
        return dfs(node)
