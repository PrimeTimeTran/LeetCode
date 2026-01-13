class Solution:
    def smaller_first(self, n1: List[int], n2: List[int]):
        m, n = len(n1), len(n2)
        if m < n:
            m, n, n1, n2 = n, m, n2, n1
        return (m, n, n1, n2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, l1, l2 = self.smaller_first(nums1, nums2)
        l, r = 0, m
        midex = (m+n+1) // 2
        while l <= r:
            p1 = (l+r) // 2
            p2 = midex - p1
            l1_max = l1[p1-1] if p1 > 0 else -inf
            l2_max = l2[p2-1] if p2 > 0 else -inf
            r1_min = l1[p1] if p1 < m else inf
            r2_min = l2[p2] if p2 < n else inf
            if l1_max <= r2_min and l2_max <= r1_min:
                lefts_max = max(l1_max, l2_max)
                rights_min = min(r1_min, r2_min)
                if (m+n) % 2:
                    return lefts_max
                return (lefts_max + rights_min) / 2
            if l1_max > r2_min:
                r = p1 - 1
            else:
                l = p1 + 1
        return 0

class Solution:
    def shorter_first(self, n1: List[int], n2: List[int]):
        m, n = len(n1), len(n2)
        if m > n:
            m, n, n1, n2 = n, m, n2, n1
        return (m, n, n1, n2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, l1, l2 = self.shorter_first(nums1, nums2)
        l, r = 0, m
        midex = (m+n+1) // 2
        while l <= r:
            p1 = (l+r) // 2
            p2 = midex - p1
            l1_max = l1[p1 - 1] if p1 > 0 else -inf
            l2_max = l2[p2 - 1] if p2 > 0 else -inf
            r1_min = l1[p1] if p1 < m else inf
            r2_min = l2[p2] if p2 < n else inf

            if l1_max <= r2_min and l2_max <= r1_min:
                lefts_max = max(l1_max, l2_max)
                rights_min = min(r1_min, r2_min)
                if (m+n) % 2:
                    return lefts_max
                return (lefts_max + rights_min) / 2
            elif l1_max > r2_min:
                r = p1 - 1
            else:
                l = p1 + 1
        return 0

# class Solution:
#     def setShorterLengthInvariant(self, n1, n2):
#         m, n = len(n1), len(n2)
#         if m > n:
#             n1, n2, m, n = n2, n1, n, m
#         return (n1, n2, m, n)
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l1, l2, m, n = self.setShorterLengthInvariant(nums1, nums2)
#         l, r = 0, m
#         midex = (m+n+1) // 2
#         while l <= r:
#             p1 = (l+r) // 2
#             p2 = midex - p1
#             l1_max = l1[p1-1] if p1 > 0 else -inf
#             l2_max = l2[p2-1] if p2 > 0 else -inf
#             r1_min = l1[p1] if p1 < m else inf
#             r2_min = l2[p2] if p2 < n else inf
#             if l1_max <= r2_min and l2_max <= r1_min:
#                 lefts_max = max(l1_max, l2_max)
#                 rights_min = min(r1_min, r2_min)
#                 if (m+n) % 2:
#                     return lefts_max
#                 return (lefts_max + rights_min) / 2
#             elif l1_max > r2_min:
#                 r = p1 - 1
#             else:
#                 l = p1 + 1
#         return 0