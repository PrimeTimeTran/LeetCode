class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        num_of_rows, num_of_cols = len(matrix), len(matrix[0])

        front, back = 0, (num_of_rows)*(num_of_cols) - 1

        while front <= back:
            midpoint = front + ((back - front) // 2)
            number = matrix[midpoint // num_of_cols][midpoint % num_of_cols]

            if number == target: return True
            elif number < target:
                front = midpoint + 1
            else:
                back = midpoint - 1

        return False