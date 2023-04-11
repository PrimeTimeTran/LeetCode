class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        

        return ''.join(stack)