'''
Create a set from nums. 
Iterate items and check if the current n - 1 is not in nums, set cur and begin a loop which grows cur.
The while loop should increment while n+cur is in nums. Increment by 1
After the loop update res to max of res and cur
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, cur, nums = 0, 0, set(nums)
        for n in nums:
            if n-1 not in nums:
                cur = 0
                while n + cur in nums:
                    cur += 1
                res = max(res, cur)
        return res

