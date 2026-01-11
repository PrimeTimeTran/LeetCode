class Solution:
    area = 0
    def maximalRectangle(self, matrix) -> int:
        def shark(a, i, j, len_row):
            leftEdge = j 
            rightEdge = leftEdge + len_row - 1
            flag = True
            if rightEdge >= len(a[0]): return
            if i+1 >= len(a): return 
            for _ in range(leftEdge, rightEdge+1):
                el = a[i+1][_]
                if a[i+1][_] != '1':
                    flag = False
                    break
            if flag:
                self.area += len_row
                shark(a, i+1, j, len_row)
            else: return 
        a = matrix
        rows = len(a)
        cols = len(a[0])
        max_possible_area = 0
        for _row in a:
            for _el in _row:
                if _el == '1':
                    max_possible_area += 1
        if max_possible_area == rows * cols:
            return rows * cols
        self.area = 0
        max_area = 0
        
        for i in range(rows):
            len_row = 0
            for j in range(cols):
                self.area = 0
                if a[i][j] == '0':
                    len_row = 0
                if a[i][j] == '1':
                    len_row += 1
                    self.area = len_row
                if j+1 == len(a[i]):
                    if a[i][j] == '1':
                        temp = len_row
                        for _ in range(j-len_row+1, j+1): # текущий левый элемент
                            for __ in range(1, len_row+1): # текущая длина среза
                                self.area = __
                                shark(a, i, _, __)
                                max_area = max(self.area, max_area)
                                self.area = 0

                            len_row -= 1
                else:
                    if a[i][j] == '1' and a[i][j+1] != '1':
                        temp = len_row
                        for _ in range(j-len_row+1, j+1): # текущий левый элемент
                            for __ in range(1, len_row+1): # текущая длина среза
                                self.area = __
                                shark(a, i, _, __)
                                max_area = max(self.area, max_area)
                                self.area = 0
                            len_row -= 1
        return max_area