class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(a) != sorted(a) for a in zip(*strs))