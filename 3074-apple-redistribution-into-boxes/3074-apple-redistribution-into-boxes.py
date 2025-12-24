class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        res = 0
        for i, c in enumerate(capacity):
            total -= c
            res += 1
            if total <= 0: break
        return res