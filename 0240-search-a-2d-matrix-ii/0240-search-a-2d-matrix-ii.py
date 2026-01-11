class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            cell = mat[r][c]
            if cell == target:
                return True
            elif cell < target:
                r += 1
            else:
                c -= 1
        return False