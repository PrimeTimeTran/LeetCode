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
        def dp(i, holding, count):
            if i == n or count == k:
                return 0
            skip = dp(i+1, holding, count)
            if holding:
                sell = prices[i] + dp(i+1, not holding, count+1)
                return max(skip, sell)
            else:
                buy = -prices[i] + dp(i+1, not holding, count)
                return max(skip, buy)
        return dp(0, False, 0)