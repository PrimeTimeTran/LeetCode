class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            val = mat[r][c]
            if val == target: return True
            elif val > target:
                c -= 1
            else:
                r += 1
        return False

# class Solution:
#     def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
#         rows, cols = len(mat), len(mat[0])
#         r, c = 0, cols - 1
#         while r < rows and c >= 0:
#             cur = mat[r][c]

#             if cur == target:
#                 return True
#             elif cur > target:
#                 c -= 1
#             else:
#                 r += 1
#         return False