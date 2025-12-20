class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt, head.next = head.next, prev
            head, prev = nxt, head
        return prev