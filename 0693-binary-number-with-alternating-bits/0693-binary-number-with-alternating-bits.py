'''
Diagram
n = 5

n       = 1 0 1
n>>1    = 0 1 0
XOR     = 1 1 1  <-- all 1s
x+1     = 1 0 0 0
x & x+1 = 0        <-- equals 0 → True
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0