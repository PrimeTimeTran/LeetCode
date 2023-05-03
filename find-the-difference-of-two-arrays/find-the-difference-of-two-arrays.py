class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer.append(set([n for n in nums1 if n not in nums2]))
        answer.append(set([n for n in nums2 if n not in nums1]))

        print(answer)
        return answer