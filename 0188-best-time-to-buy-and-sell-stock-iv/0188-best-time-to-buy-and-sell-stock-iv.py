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
        def dp(i, holding, completed_count):
            if i == n or completed_count == k:
                return 0
            price = prices[i]
            i+=1
            skip = dp(i, holding, completed_count)
            completed_count += 1 if holding else 0
            # If you're holding you previous bought(debitted) and must now sell(credit)
            cashflow_realized = price if holding else -price
            # 
            act = cashflow_realized + dp(i, not holding, completed_count)
            return max(skip, act)
        return dp(0, False, 0)