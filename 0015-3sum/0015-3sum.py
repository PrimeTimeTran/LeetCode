'''
1. Understand
    - We've given nums which is a list of nums.
    - We want to return a list of lists where each sublist is the numbers which sum to 0.
2. Pseudocode
    1. Sort nums
    2. Iterate numbers, setting l pointer to current index + 1 and r pointer to len(nums).
    3. Close window until we're out of bounds
    4. On each iteration check that the sum of the numbers <, >, or == 0. If 0 then append the list of current of nums.
    5. Check if we can close our window more within the current iteration because we don't want duplicates.

    - Make sure to check for equality between indexes.

3. Diagram
nums = [-1, 0, 1, 2,-1,-4]
nums = [-4,-1,-1, 0, 1, 2]
               c  l     r
0: -4,
    l = -1
    r = 2
    ... []
1: -1
    l = -1
    r = 2
    append [-1,-1,2]



4. Code
5. Big O
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
        return res