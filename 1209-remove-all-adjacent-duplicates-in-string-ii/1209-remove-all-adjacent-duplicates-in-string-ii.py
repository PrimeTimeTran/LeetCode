'''
deeedbbcccbdaa

[[a1][a2]]

'''

class Solution:
    def removeDuplicates(self, string: str, k: int) -> str:
        s = []
        for c in string:
            if len(s) > 0:
                if s and s[-1][0] == c:
                    prev = s[-1][1]
                    if prev == k - 1:
                        for _ in range(k-1):
                            s.pop()
                    else:
                        s.append([c,prev+1])
                else:
                    s.append([c,1])
            else:
                s.append([c,1])
        s = [t[0] for t in s]
        return "".join(s)