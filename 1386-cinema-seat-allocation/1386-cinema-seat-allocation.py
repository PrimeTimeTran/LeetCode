from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] |= 1 << (s - 2)
        result = (n - len(rows)) * 2
        LEFT  = 0b00001111  # 2,3,4,5
        MIDDLE = 0b00111100 # 4,5,6,7
        RIGHT = 0b11110000  # 6,7,8,9
        for mask in rows.values():
            left = not (mask & LEFT)
            right = not (mask & RIGHT)
            middle = not (mask & MIDDLE)

            if left and right:
                result += 2
            elif left or right or middle:
                result += 1

        return result