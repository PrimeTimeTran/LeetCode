'''
1. Understand
We're searching for...
max(left) <= min(right)

- Understand why the partition condition works
- Recognize this as a “binary search on partition size”
- Be able to explain the idea at a high level
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def make_nums1_smaller(n1, n2):
            m, n = len(n1), len(n2)
            if m > n:
                n1, n2, m, n = n2, n1, n, m
            return (n1, n2, m, n)

        nums1, nums2, m, n = make_nums1_smaller(nums1, nums2)
        low, high, is_odd_length = 0, m, (m + n) % 2 == 1
        half_len = (m + n + 1) // 2 
        
        while low <= high:
            # Choose P1: number of elements taken from nums1 into the left partition [0, P1)
            P1 = (low + high) // 2
            # Define P2 as the number of elements taken from nums2 into the left partition [0, P2)
            # such that the total size of the left partition is half_len.
            P2 = half_len - P1
            # L1: last element on the left side of nums1
            L1 = nums1[P1 - 1] if P1 > 0 else -inf
            # R1: first element on the right side of nums1
            R1 = nums1[P1] if P1 < m else inf
            # L2: last element on the left side of nums2
            L2 = nums2[P2 - 1] if P2 > 0 else -inf
            # R2: first element on the right side of nums2
            R2 = nums2[P2] if P2 < n else inf
            if L1 <= R2 and L2 <= R1:
                return float(max(L1, L2)) if is_odd_length else (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                # L1 is too large, meaning the cut P1 is too far to the right.
                # Move the cut P1 to the left.
                high = P1 - 1
            else:
                # Otherwise (L2 > R1),
                # the cut P1 is too far to the left.
                # Move the cut P1 to the right.
                low = P1 + 1
        return 0.0