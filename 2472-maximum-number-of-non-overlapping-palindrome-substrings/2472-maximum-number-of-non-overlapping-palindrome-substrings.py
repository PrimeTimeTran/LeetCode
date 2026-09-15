class Solution:
  def maxPalindromes(self, s: str, k: int) -> int:
    n = len(s)
    if k == 1:
      return n
    res = i = 0
    while i <= n - k:
      for d in (k, k + 1):
        inbounds = i + d <= n
        substring = s[i : i + d]
        reversed = substring[::-1]
        valid_palindrome = substring == reversed
        if inbounds and valid_palindrome:
          res += 1  
          i += d
          break
      else:
        i += 1
    return res
