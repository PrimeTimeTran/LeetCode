'''
Iterate over each index of s
Add it's value to a running sum.
If the new value is greater than k, increment count, and reset sum to current digit



'165462'


ans = 4
cur = 2
2



'''

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur, ans = 0, 1
        
        for d in s:
            if int(d) > k: return -1
            
            cur = 10*cur + int(d)
            
            if cur > k:
                ans+=1
                cur = int(d)
        return ans
            