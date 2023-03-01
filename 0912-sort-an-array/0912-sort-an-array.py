class Solution:
  def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr

        midIdx = len(arr) // 2
        l = arr[:midIdx]
        r = arr[midIdx:]
        return self.merge(self.sortArray(l), self.sortArray(r))

  def merge(self, left, right):
      res = []
      l = r = 0
      while l < len(left) and r < len(right):
          if left[l] < right[r]:
              res.append(left[l])
              l += 1
          else:
              res.append(right[r])
              r += 1
      res.extend(left[l:])
      res.extend(right[r:])

      return res
