# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, count = head, 0
        while n and count < k:
            n = n.next
            count+=1
        if count < k: return head
        new_head, prev = self.reverse(head, k)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count, prev = None):
        while count > 0:
            nxt, head.next = head.next, prev
            prev, head = head, nxt
            count-=1
        return [head, prev]
        