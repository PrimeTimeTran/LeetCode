'''
1. 
n - 1 will flip the least significant 1 to 0. All other 0 bits to the right of this bit become a 1
n & n-1 "persists" the 0's after switching the least significant set bit to 0(maintains 0s right of it).
'''
class Solution:
  def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
        res += 1
        n &= n-1
    return res