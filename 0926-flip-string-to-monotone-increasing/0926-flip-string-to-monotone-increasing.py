class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        stack = []
        res = 0
        for ch in s :
            if stack and stack[-1] == "1" and ch == "0" :
                stack.pop()
                res +=1
            else :
                stack.append(ch)
        return res