class Solution:
    def minStartValue(self, A: List[int]) -> int:
        return -min(0, min(accumulate(A))) + 1
