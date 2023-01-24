class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        for r in matrix:
            if r[0] <= t <= r[-1]:
                i = bisect.bisect_left(r, t)
                if r[i] == t:
                    return True
                else:
                    return False
        return False