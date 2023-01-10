# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = {}
        while headA:
            seen[headA] = headA
            headA = headA.next
        while headB:
            print(headB.val)
            if headB in seen:
                return seen[headB]
            headB = headB.next

        return None