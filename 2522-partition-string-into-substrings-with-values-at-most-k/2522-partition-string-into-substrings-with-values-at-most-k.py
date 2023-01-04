'''
Iterate through each digit in s. Add it as one's place to cur number.

Compare new cur with k, if larger then increment ans and reset cur to be digit

Return ans
'''

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur,ans = 0, 1
        for d in s:
            if int(d) > k: return -1
            cur = 10*cur+int(d)
            if cur > k:
                ans+=1
                cur = int(d)
        return ans