class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        s = f = d
        while n > 0:
            f = f.next
            n-=1
        while f.next and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return d.next