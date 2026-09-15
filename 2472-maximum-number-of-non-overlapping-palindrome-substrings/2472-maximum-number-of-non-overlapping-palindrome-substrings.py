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
        reversed_substring = substring[::-1]
        is_palindrome = substring == reversed_substring
        if inbounds and is_palindrome:
          res += 1  
          i += d
          break
      else:
        i += 1
    return res
