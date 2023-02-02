class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)
        res = []
        for w in words:
            res.append(w[::-1])
        return ' '.join(res)