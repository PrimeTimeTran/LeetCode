class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.t = k
        self.k = k

    def consec(self, num: int) -> bool:
        if self.t > 0:
            self.t -= 1
            
        if num != self.val:
            self.t = self.k
        
        return False if self.t else True
