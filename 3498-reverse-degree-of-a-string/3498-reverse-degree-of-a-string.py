class Solution:
  def reverseDegree(self, s: str) -> int:
    total = 0
    values = {
        c: 26 - (ord(c) - ord('a'))
        for c in string.ascii_lowercase
    }
    for i, c in enumerate(s, 1):
        total += values[c] * i
    return total