# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node

        return tolist(toint(l1) + toint(l2))