class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        items = set(nums)
        target = k 
        while target <= maximum:
            if target not in items:
                return target
            target += k
            print(k, target)
        return target

