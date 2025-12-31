'''
1. Understand
Greedy approach:
1. If total gas < total cost, completing the circuit is impossible.
2. Iterate through stations, tracking current tank. 
   - If tank becomes negative, reset tank and move the start candidate to the next station.
3. The last start candidate after the loop is the answer.


5. Big O
Time:   O(m + n) where m is the length of gas and n is the length of cost because we sum their values
Space:  O(1) because we only track a few variables
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        s = t = 0
        for i in range(len(gas)):
            t += (gas[i] - cost[i])
            if t < 0:
                t = 0
                s = i+1
        return s