class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(v):
            res = 0
            while v != 0:
                res+=1
                v = v & v-1
            return res
            
        res = []
        for i in range(n+1):
            val = countOnes(i)
            res.append(val)
            
        return res

# 0000000        
# 128,64,32,16,8,4,2,1