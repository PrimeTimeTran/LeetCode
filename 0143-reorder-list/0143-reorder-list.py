class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        prev = None
        while s:
            nxt = s.next
            s.next = prev
            prev = s
            s = nxt
        l1, reversed_list = head, prev
        while l1 and reversed_list:
            tmp1, tmp2 = l1.next, reversed_list.next
            l1.next, reversed_list.next = reversed_list, tmp1
            l1, reversed_list = tmp1, tmp2