# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def getIndex(self, rd: 'ArrayReader') -> int:
        l, r = 0, rd.length() - 1
        while l < r:
            h = (r - l + 1) // 2  # half, h * 2 <= r - l + 1
            if rd.compareSub(l, l + h - 1, l + h, l + h * 2 - 1) != 1:
                l = l + h
            else:
                r = l + h - 1
        return l