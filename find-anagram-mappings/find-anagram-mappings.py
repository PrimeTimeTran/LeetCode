class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        for c in nums1:
            mapping.append(nums2.index(c))
        return mapping