from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        items = defaultdict(list)

        for r, s in reservedSeats:
            items[r].append(s)

        total = (n - len(items)) * 2

        for seats_in_row in items.values():
            seats = set(seats_in_row)

            left  = not any(s in seats for s in [2, 3, 4, 5])
            right = not any(s in seats for s in [6, 7, 8, 9])
            middle = not any(s in seats for s in [4, 5, 6, 7])

            if left and right:
                total += 2
            elif left or right or middle:
                total += 1

        return total