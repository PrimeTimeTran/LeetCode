class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        rows, cols = len(mat), len(mat[0])

        r, c = 0, cols - 1

        while r < rows and c >= 0:
            cur = mat[r][c]

            if cur == target:
                return True
            elif cur > target:
                # eliminate column c
                c -= 1
            else:
                # eliminate row r
                r += 1

        return False
