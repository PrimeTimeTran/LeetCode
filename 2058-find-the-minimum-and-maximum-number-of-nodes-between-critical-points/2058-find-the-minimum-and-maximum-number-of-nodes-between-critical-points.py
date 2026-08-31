# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        critical = []
        index = 1

        while cur and cur.next:
            prev = cur
            cur = cur.next

            if cur.next:
                if (cur.val > prev.val and cur.val > cur.next.val) or \
                   (cur.val < prev.val and cur.val < cur.next.val):
                    critical.append(index)

            index += 1

        if len(critical) < 2:
            return [-1, -1]

        # Minimum distance between consecutive critical points
        min_dist = min(
            critical[i] - critical[i - 1]
            for i in range(1, len(critical))
        )

        # Maximum distance is first -> last
        max_dist = critical[-1] - critical[0]

        return [min_dist, max_dist]