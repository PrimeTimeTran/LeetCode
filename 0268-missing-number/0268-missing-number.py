class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    s = 0
    for n in nums:
      s ^= n
    for i in range(len(nums)+1):
      s ^= i
    return s