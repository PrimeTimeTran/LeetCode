class Solution:
    def reverseDegree(self, s: str) -> int:
        lowercase_str = string.ascii_lowercase
        reversed = list(lowercase_str)[::-1]
        total = 0
        for i, c in enumerate(s):
          total += (reversed.index(c)+1) * (i+1)
          # total += contribution
        return total