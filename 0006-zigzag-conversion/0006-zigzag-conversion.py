class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, ver = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                ver = 1
            elif index == numRows -1:
                ver = -1
            index += ver
        return ''.join(L)