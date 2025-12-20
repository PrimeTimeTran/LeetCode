class Solution:
    def findClosestElements(self, A, k, x):
        l, r = 0, len(A) - k
        while l < r:
            m = (l + r) // 2
            if x - A[m] > A[m + k] - x:
                l = m + 1
            else:
                r = m
        return A[r:r + k]