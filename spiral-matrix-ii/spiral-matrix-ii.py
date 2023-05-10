class Solution:
    def generateMatrix(self, n):
        matrix = []
        if not n: return matrix
        for row in range(n):
            rowArray = []
            for col in range(n):
                rowArray.append(0)
            matrix.append(rowArray)
        num = 1
        top = 0
        right = n - 1
        down = n - 1
        left = 0
        while left <= right and top <= down: 
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1 
            down -= 1
            for i in range(down, top-1, -1):
                matrix[i][left] = num 
                num += 1
            left += 1
        return matrix