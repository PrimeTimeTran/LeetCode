class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        target = max(candies)
        for n in candies:
            if n+extraCandies >= target:
                result.append(True)
            else:
                result.append(False)
        return result