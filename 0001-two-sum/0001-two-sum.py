
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, n in enumerate(nums):
            complement = target - n
            if store.get(complement) != None:
                return [i, store.get(complement)]
            store[n] = i