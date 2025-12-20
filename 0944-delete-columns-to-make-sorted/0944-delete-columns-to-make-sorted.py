class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i, iChar in enumerate(strs[0]):
            for j in range(1, len(strs)):
                char = strs[j][i]
                if strs[j-1][i] > strs[j][i]:
                    res += 1
                    break
        return res
