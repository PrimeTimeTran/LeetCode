'''
1. Understand
We're searching for...
max(left) <= min(right)

- Understand why the partition condition works
- Recognize this as a “binary search on partition size”
- Be able to explain the idea at a high level
'''
class Solution:
    def shorter_first(self, n1, n2):
        m, n = len(n1), len(n2)
        if m > n:
            n1, n2, m, n = n2, n1, n, m
        return (n1, n2, m, n)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We maintain the invariant that list1 is the shorter array.
        # This guarantees safe partition indices and simplifies boundary handling.
        list1, list2, m, n = self.shorter_first(nums1, nums2)
        l, r = 0, m
        midex = (m + n + 1) // 2
        while l <= r:
            P1 = (l + r) // 2
            # Derived partition of longer list from shorter list invariant
            P2 = midex - P1
            # P defines a partition boundary:
            #   list[:P]  is the left partition
            #   list[P:]  is the right partition
            # P-1 is therefore the max element on the left,
            # and P is the min element on the right.
            # We guard P == 0 and P == len(list) to handle empty partitions safely.
            l1_max = list1[P1 - 1] if P1 > 0 else -inf
            l2_max = list2[P2 - 1] if P2 > 0 else -inf
            r1_min = list1[P1] if P1 < m else inf
            r2_min = list2[P2] if P2 < n else inf
            if l1_max <= r2_min and l2_max <= r1_min:
                lefts_max = max(l1_max, l2_max)
                rights_min = min(r1_min, r2_min)
                if (m + n) % 2:
                    return float(lefts_max)
                return (lefts_max + rights_min) / 2
            elif l1_max > r2_min:
                r = P1 - 1
            else:
                l = P1 + 1
        return 0