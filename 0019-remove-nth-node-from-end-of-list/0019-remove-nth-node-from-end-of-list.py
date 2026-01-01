class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = f = tail = ListNode(0, head)
        while n > 0:
            f = f.next
            n-=1
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return tail.next