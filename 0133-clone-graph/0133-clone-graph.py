class Solution:
    def cloneGraph(self, node: Optional['Node'], seen = {}) -> Optional['Node']:
        def dfs(n):
            if not n: return
            if n in seen: return seen[n]
            node = Node(n.val)
            seen[n] = node
            for nei in n.neighbors:
                node.neighbors.append(dfs(nei))
            return node
        return dfs(node) if node else None