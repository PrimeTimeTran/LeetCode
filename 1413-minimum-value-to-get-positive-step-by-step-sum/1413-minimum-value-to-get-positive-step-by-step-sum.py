class Solution:
    def minStartValue(self, A: List[int]) -> int:
        return -min(min(accumulate(A)), 0)+1