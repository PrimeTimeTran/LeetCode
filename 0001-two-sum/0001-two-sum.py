class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    
    for i, n in enumerate(nums):
      diff = target - n
      if diff in seen:
        return [i, seen[diff]]
      else:
        seen[n] = i