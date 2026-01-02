class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        prev = None
        while s:
            nxt, s.next = s.next, prev
            prev, s = s, nxt
        l1, l2 = head, prev
        while l1 and l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next, l2.next = l2, tmp1
            l1, l2 = tmp1, tmp2