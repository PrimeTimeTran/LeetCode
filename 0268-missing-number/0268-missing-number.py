class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    s=0
    for e in nums:
      s=s^e
    for i in range(len(nums)):
      s=s^i
    s=s^(i+1)
    return s