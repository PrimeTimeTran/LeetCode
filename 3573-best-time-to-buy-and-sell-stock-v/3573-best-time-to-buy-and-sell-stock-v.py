'''
1. Understand
Return an int representing the maximum profit you can make making at most k transactions.
DP because it's asking to find the best given the constraint k from a list of subproblems.

2. Diagram
3. Pseudocode
4. Code
5. Big O
Time:   O()
Space:  O()
'''
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # i             =   day/price
        # remaining     =   how many transactions remaining
        # carry         =   action of carries forward prev state. 
        #                   -1      =   free
        #                   0       =   sold
        #                   1       =   bought
        @lru_cache(maxsize=1000*4)
        def dp(i, rem, carry):
            if i == len(prices) or rem == 0:
                return 0 if carry == -1 else -inf
            p, mx = prices[i], -inf
            if carry > -1:
                if carry == 0:
                    mx = dp(i+1, rem - 1, -1) - p
                else:
                    mx = dp(i+1, rem - 1, -1) + p
            else:
                mx = max(
                    # Sell
                    dp(i+1, rem, 0) + p,
                    # Buy
                    dp(i+1, rem, 1) - p,
                )
            return max(dp(i+1, rem, carry), mx)
        return dp(0, k, -1)