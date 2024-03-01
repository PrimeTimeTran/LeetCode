# 1. Understand
# - Take an input array and return true if element appears more than once in the array.
# - 
# 2. Diagram
# nums = [1,2,3,4,5,5] -> nums = [1,2,3,4,5]
# 
# 3. Pseudocode
# 3. Code

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)