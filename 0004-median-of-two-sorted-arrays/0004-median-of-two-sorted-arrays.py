class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = heapq.merge(nums1,nums2)
        final = list(final)
        
        if len(final) % 2 == 0:
            l = int(len(final)/2) - 1
            r = int(len(final)/2)
            return (final[l]+final[r]) /2 
        else:
            return final[len(final) //2]