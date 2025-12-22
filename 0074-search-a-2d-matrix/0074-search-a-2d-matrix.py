class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R * C - 1
        while l <= r:
            m = (l + r) // 2
            dr, dc = divmod(m, C)
            val = matrix[dr][dc]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False