class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = ListNode(0, head)
        s, f = d, d
        # Find the middle of the list
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # Reverse the second half(we researched half way by using above logic)
        prev = None
        while s:
            nxt, s.next = s.next, prev
            prev, s = s, nxt

        l1, reversed_half = head, prev
        while l1 and reversed_half:
            tmp1, tmp2 = l1.next, reversed_half.next
            l1.next, reversed_half.next = reversed_half, tmp1
            l1, reversed_half = tmp1, tmp2