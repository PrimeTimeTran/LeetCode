# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
243+564 = 807
342+465 = 807
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def tolist(num):
            n = ListNode(num % 10)
            if num > 9: n.next = tolist(num // 10)
            return n
        def toint(n):
            return n.val + 10 * toint(n.next) if n else 0
        return tolist(toint(l1) + toint(l2))