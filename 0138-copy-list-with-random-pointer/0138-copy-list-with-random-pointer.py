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
        while d:
            store[d] = Node(d.val, None, None)
            d = d.next
        d = head
        while d:
            if d.next: 
                store[d].next = store[d.next]
            if d.random: 
                store[d].random = store[d.random]
            d = d.next
        return store[head]