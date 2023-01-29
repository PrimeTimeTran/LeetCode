class StockSpanner:
  def __init__(self):
      self.stack = []

  def next(self, price):
      res = 1
      while self.stack and self.stack[-1][0] <= price:
          res += self.stack.pop()[1]
      self.stack.append([price, res])
      return res

#     def __init__(self):
#         self.prices = []

#     def next(self, price: int) -> int:
#         self.prices.append(price)
#         res = 0
#         for i in range(len(self.prices) -1,-1,-1):
#           if self.prices[i] <= price:
#             res+=1
#           else:
#             break
#         return res
        


# # # Your StockSpanner object will be instantiated and called as such:
# # # obj = StockSpanner()
# # # param_1 = obj.next(price)