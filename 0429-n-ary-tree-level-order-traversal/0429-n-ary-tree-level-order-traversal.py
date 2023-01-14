"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    for nei in cur.children:
                        q.append(nei)
            if level:
                res.append(level)
        return res