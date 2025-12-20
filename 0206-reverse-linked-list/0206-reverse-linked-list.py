# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using a loop capture the next value and update the head's next value to be previous
# Update the previous value to be current head and head's value to be next
# When we no longer have a head, return the previous value
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt, head.next = head.next, prev
            head, prev = nxt, head
        return prev