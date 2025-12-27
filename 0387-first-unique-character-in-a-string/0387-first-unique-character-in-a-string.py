class Solution:
  def firstUniqChar(self, s: str) -> int:
    items = {}
    for c in s:
      items[c] = items.get(c, 0 ) + 1
      
    for i, c in enumerate(s):
      if items[c] == 1:
        return i
    return -1
        