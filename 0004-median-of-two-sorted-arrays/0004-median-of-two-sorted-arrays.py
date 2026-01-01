'''
1. Understand
We're searching for...
max(left) <= min(right)

- Understand why the partition condition works
- Recognize this as a “binary search on partition size”
- Be able to explain the idea at a high level
'''
class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        def shorter_first(n1, n2):
            m, n = len(n1), len(n2)
            if m > n:
                n1, n2, m, n = n2, n1, n, m
            return (n1, n2, m, n)

        l1, l2, m, n = shorter_first(l1, l2)
        l, r, is_odd_length = 0, m, (m + n) % 2 == 1
        half_len = (m + n + 1) // 2 
        
        while l <= r:
            P1 = (l + r) // 2
            P2 = half_len - P1
            l1_max = l1[P1 - 1] if P1 > 0 else -inf
            r1_min = l1[P1] if P1 < m else inf
            l2_max = l2[P2 - 1] if P2 > 0 else -inf
            r2_min = l2[P2] if P2 < n else inf
            if l1_max <= r2_min and l2_max <= r1_min:
                if is_odd_length:
                    return float(max(l1_max, l2_max))  
                else: 
                    return (max(l1_max, l2_max) + min(r1_min, r2_min)) / 2
            elif l1_max > r2_min:
                r = P1 - 1
            else:
                l = P1 + 1
        return 0.0