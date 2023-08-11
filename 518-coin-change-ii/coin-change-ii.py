class Solution:
    # Top down recursive brute
    # def change(self, amount: int, coins: List[int]) -> int:
    #     if amount == 0: 
    #         return 1 
    #     if amount < 0 or len(coins) == 0:
    #         return 0 
    #     return self.change(amount - coins[-1], coins) + self.change(amount, coins[:-1]) 
    
    # Top down recursive memo
    def change(self, amount: int, coins: List[int], dic = {}) -> int:
        if (amount,tuple(coins)) in dic:
            return dic[(amount,tuple(coins))]
        if amount == 0: 
            return 1 
        if amount < 0 or len(coins) == 0:
            return 0 
        dic[(amount,tuple(coins))]= self.change(amount - coins[-1], coins) + self.change(amount, coins[:-1]) 
        return dic[(amount,tuple(coins))]

    # Bottom up tabulation
    # def change(self, amount: int, coins: List[int]) -> int:
    #     dp = [0] * (amount + 1)
    #     dp[0] = 1
    #     for i in coins:
    #         for j in range(1, amount + 1):
    #             if j >= i:
    #                 dp[j] += dp[j - i]
    #     return dp[amount]