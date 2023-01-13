'''
[4,3]
4,4,4,3
f,f,t,f

'''

class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.o = k

    def consec(self, num: int) -> bool:
        if self.k > 0:
            self.k -= 1
        if self.val != num:
            self.k = self.o
        return False if self.k else True

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)