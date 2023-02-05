class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        for l in range(1, n+1, 2):
            for i in range(n-l+1):
                res += sum(A[i:i+l])
        return res