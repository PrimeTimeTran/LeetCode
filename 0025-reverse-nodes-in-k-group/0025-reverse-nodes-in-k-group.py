# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, n = 0, head
        while n and count < k:
            count+=1
            n = n.next
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, count)
        return prev
    def reverse(self, head, count, prev = None):
        while count > 0:
            nxt, head.next = head.next, prev
            prev, head = head, nxt
            count -= 1
        return (head, prev)