class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0 # nums[0] + nums[1] + ... + nums[middleIndex-1]
        right = sum(nums) # nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]

        for i, num in enumerate(nums): # we can use normal for loop as well.
            right -= num # as we are trying to find out middle index so iteratively we`ll reduce the value of right to find the middle index
            if left == right: # comparing the values for finding out the middle index.
                return i # if there is any return the index whixh will be our required index.
            left += num # we have to add the num iteratively. 

        return -1