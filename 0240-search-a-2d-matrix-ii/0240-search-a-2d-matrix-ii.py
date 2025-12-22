class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            if mat[i][0] <= target and mat[i][-1] >= target:
                l, r = 0, n
                while l < r:
                    m = (l + r) // 2
                    if mat[i][m] == target:
                        return True
                    elif mat[i][m] < target:
                        l = m + 1
                    else:
                        r = m
        return False