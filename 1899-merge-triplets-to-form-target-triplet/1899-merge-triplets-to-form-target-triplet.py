class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a, b, c = max(a, x), max(b, y), max(c, z)
        return [a, b, c] == target