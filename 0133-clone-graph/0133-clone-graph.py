class Solution:
    def cloneGraph(self, n: Optional['Node'], seen=None) -> Optional['Node']:
        if not n: return None
        if seen is None:
            seen = {}
        if n in seen: return seen[n]
        seen[n] = Node(n.val)
        for nei in n.neighbors:
            seen[n].neighbors.append(self.cloneGraph(nei, seen))
        return seen[n]