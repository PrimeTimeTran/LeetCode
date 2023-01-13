class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if len(stack) > 0:
                if len(stack) and stack[-1][0] == c:
                    prev = stack[-1][1]
                    if prev == k-1:
                        for _ in range(k-1):
                            stack.pop()
                    else:
                        stack.append([c,prev+1])
                else:
                    stack.append([c, 1])
            else:
                stack.append([c,1])
            
        stack = [t[0] for t in stack]
        return "".join(stack)