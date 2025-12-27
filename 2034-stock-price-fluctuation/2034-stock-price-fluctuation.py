import heapq

class StockPrice:
    def __init__(self):
        self.time_price = {}  # timestamp -> price
        self.max_heap = []    # (-price, timestamp)
        self.min_heap = []    # (price, timestamp)
        self.latest_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.time_price[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        self.latest_time = max(self.latest_time, timestamp)

    def current(self) -> int:
        return self.time_price[self.latest_time]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_heap[0]
            price = -price
            if self.time_price[timestamp] == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_heap[0]
            if self.time_price[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
