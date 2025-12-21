'''
1. Understand
We should be returning an integer representing the sum profit we might receive
If we buy/sell optimally.

2. Diagram
3. Pseudocode
- Define a top memo function which expands from day 0 to the end.
    - Identify base cases which prevent Stack Overflows. 
    - Perform a "reduction" of the problem space such that it gets closer to the base case....
    - "Do business logic..."
- Subproblem
- Base Case
- Top Down Memo
    - Recursive
- Bottom Up Tab
    - Create a store and build on it.
4. Code
5. BigO
Time:    O()
Space:   O()
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, count: int) -> int:
            if i == n or count == 0:
                return 0
            opened = count % 2 == 0
            price = prices[i]
            skip = dp(i + 1, count)
            if opened:
                take = -price + dp(i + 1, count - 1)
            else:
                take = price + dp(i + 1, count - 1)
            return max(skip, take)
        return dp(0, k * 2)
        # n = len(prices)
        # best = 0
        # # (day, transactions_left, holding, profit)
        # stack = [(0, k, False, 0)]
        # while stack:
        #     i, t, holding, profit = stack.pop()
        #     if i == n or t == 0:
        #         best = max(best, profit)
        #         continue
        #     # Option 1: skip day
        #     stack.append((i+1, t, holding, profit))
        #     # Option 2: transact
        #     if not holding:
        #         # buy
        #         stack.append((i+1, t, True, profit - prices[i]))
        #     else:
        #         # sell
        #         stack.append((i+1, t-1, False, profit + prices[i]))

        # return best

        # n = len(prices)
        # NEG_INF = -10**15

        # dp = [[NEG_INF] * (2*k + 1) for _ in range(n+1)]

        # # Base cases
        # for count in range(2*k + 1):
        #     dp[n][count] = 0 if count % 2 == 0 else NEG_INF

        # for i in range(n):
        #     dp[i][0] = 0

        # # Fill bottom-up
        # for i in range(n-1, -1, -1):
        #     for count in range(1, 2*k + 1):
        #         opened = count % 2 == 0
        #         sign = -1 if opened else 1

        #         take = dp[i+1][count-1] + sign * prices[i]
        #         skip = dp[i+1][count]

        #         dp[i][count] = max(take, skip)

        # return dp[0][2*k]
