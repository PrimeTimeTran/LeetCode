class Solution:
    def removeDuplicates(self, string: str, k: int) -> str:
        s = []
        for c in string:
            if len(s) > 0:
                if len(s) and s[-1][0] == c:
                    p = s[-1][1]
                    if p == k-1:
                        for _ in range(k-1):
                            s.pop()
                    else:
                        s.append([c, p+1])
                else:
                    s.append([c,1])
            else:
                s.append([c, 1])
        res = [t[0] for t in s]
        return "".join(res)