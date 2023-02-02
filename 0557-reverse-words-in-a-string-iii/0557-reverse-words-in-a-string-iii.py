class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []
        for w in words:
            res.append(w[::-1])
        return ' '.join(res)