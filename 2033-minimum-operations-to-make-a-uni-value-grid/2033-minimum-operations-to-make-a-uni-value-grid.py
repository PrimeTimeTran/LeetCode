class Solution:
    def minOperations(self, grid, x):
        items = [n for row in grid for n in row]
        base = items[0] % x
        if any(n % x != base for n in items):
            return -1

        # normalize
        items = [n // x for n in items]
        items.sort()

        median = items[len(items) // 2]

        return sum(abs(n - median) for n in items)