class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            subarrays = 1
            current_sum = 0
            for x in nums:
                if current_sum + x > max_sum:
                    subarrays += 1
                    current_sum = x
                    if subarrays > k: return False
                else:
                    current_sum += x
            return True
        l, r = max(nums), sum(nums)
        while l < r:
            arr_max = (l + r) // 2
            if can_split(arr_max):
                r = arr_max
            else:
                l = arr_max + 1
        return r