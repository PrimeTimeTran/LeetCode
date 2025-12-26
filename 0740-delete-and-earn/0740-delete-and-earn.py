'''
1. Understand
2. Diagram
3. Pseudocode
Create a counter which counts the number of instances of a number in our list

4. Code
5. BigO
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums)+1)
        for num in nums:
            dp[num] += num
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1],  dp[i]+dp[i-2])
        return dp[-1]