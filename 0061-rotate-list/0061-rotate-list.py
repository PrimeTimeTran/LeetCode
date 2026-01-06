# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        n = tail = head
        while n and n.next:
            n = n.next
            count += 1
        k %= count+1
        if k == 0: return head
        n.next = head
        for _ in range(count - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head