from collections import deque

class Solution:
    def canMeasureWater(self, x: int, y: int, targetCapacity: int) -> bool:
        seen = set()
        q = deque([(0, 0)])   # (water in x, water in y)

        while q:
            a, b = q.popleft()

            if a == targetCapacity or b == targetCapacity or a + b == targetCapacity:
                return True

            if (a, b) in seen:
                continue
            seen.add((a, b))

            # Fill operations
            q.append((x, b))
            q.append((a, y))

            # Empty operations
            q.append((0, b))
            q.append((a, 0))

            # Pour a → b
            pour = min(a, y - b)
            q.append((a - pour, b + pour))

            # Pour b → a
            pour = min(b, x - a)
            q.append((a + pour, b - pour))

        return False
