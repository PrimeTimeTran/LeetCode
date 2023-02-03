"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        while q:
            r = None
            for _ in range(len(q)):
                c = q.popleft()
                c.next, r = r, c
                if c.right:
                    q.extend([c.right, c.left])
        return root