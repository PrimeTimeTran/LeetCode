'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time: O()
Space: O()
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i, rem):
            if i == len(coins) or rem < 0:
                return 0
            if rem == 0:
                return 1
            return dp(i+1, rem) + dp(i, rem - coins[i])
        return dp(0, amount)