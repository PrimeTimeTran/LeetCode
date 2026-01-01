"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        store, d = {}, head
        def get(node):
            if node not in store:
                store[node] = Node(node.val)
            return store[node]
        while d:
            copy = get(d)
            copy.next = get(d.next) if d.next else None
            copy.random = get(d.random) if d.random else None
            d = d.next
        return store[head]
