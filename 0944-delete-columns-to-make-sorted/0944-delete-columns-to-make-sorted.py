class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # return sum(list(a) != sorted(a) for a in zip(*strs))
        res = 0
        strs = [list(s) for s in strs]
        for a in zip(*strs):
          for i in range(0, len(a)-1):
            if ord(a[i]) > ord(a[i+1]):
              res+=1
              break
        
        
        return res