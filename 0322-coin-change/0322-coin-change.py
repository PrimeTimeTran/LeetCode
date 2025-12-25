'''
1. Understand
Given a list of coins & a target amount return the minimum count of coins required to sum to amount. Each coin can be used infinite times.

1. Top Down Recursive 
We can recurse from amount until we've reached base cases. 
If remaining is < 0 or == 0 then we exit recursion. 
If remaining == 0 return 0, otherwise return infinity.

After the base cases, default to infinity as the 'best' response; then recurse on each coin to find the minimum.

Return the minimum.

2. Diagram
amount = 11
coins = [1,2,5]

3. Pseudocode
4. Code
5. Big O
Time:   O(amount × n)
Space:  O(amount)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @lru_cache(None)
        # def dp(rem):
        #     if rem == 0:
        #         return 0
        #     if rem < 0:
        #         return float('inf')
        #     best = float('inf')
        #     for c in coins:
        #         best = min(best, dp(rem - c)+1)
        #     return best
        # best = dp(amount)
        # return best if best != float('inf') else -1
        n = amount+1
        dp = [n]*(n)
        dp[0] = 0
        for a in range(n):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return dp[amount] if dp[amount] != n else -1