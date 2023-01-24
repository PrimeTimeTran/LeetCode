class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        front, back = 0, (m) * (n) - 1

        while front <= back:
            midpoint = front + ((back - front) // 2)
            number = matrix[midpoint // n][midpoint % n]

            if number == t:
                return True
            elif number < t:
                front = midpoint + 1
            else:
                back = midpoint - 1

        return False
