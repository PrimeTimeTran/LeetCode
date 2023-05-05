class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans: int = 0
            
        currCount: int = 0
            
        vowels: str = "aeiou"
            
        for i, v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans