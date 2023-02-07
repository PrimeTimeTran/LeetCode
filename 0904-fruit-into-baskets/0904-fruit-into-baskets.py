class Solution:
    def totalFruit(self, A: List[int]) -> int:
        count, l = {}, 0
        for r, v in enumerate(A):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[A[l]] -= 1
                if count[A[l]] == 0: del count[A[l]]
                l += 1
        return r - l + 1