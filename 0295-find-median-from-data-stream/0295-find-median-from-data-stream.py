from heapq import heappush,heappop

class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, n: int) -> None:
        heappush(self.max, -n)
        heappush(self.min, -heappop(self.max))
        if len(self.max) < len(self.min):
            heappush(self.max, -heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        else:
            return (float(-self.max[0] + self.min[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()