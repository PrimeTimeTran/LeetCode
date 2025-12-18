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
        @lru_cache(None)
        def dp(i, count):
            # If we've previously bought, our count should be odd
            opened = count % 2 == 0
            if i == len(prices) or count == 0:
                return 0 if opened else -inf
            price = prices[i]
            # If we've opened a position we debit, credit otherwise
            sign = -1 if opened else 1
            take = dp(i+1, count-1) + (price * sign)
            skip = dp(i+1, count)
            return max(take, skip)
        return dp(0, k*2)