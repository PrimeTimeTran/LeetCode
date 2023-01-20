class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t = [0]*(n+1)
        for a, b in trust:
            t[a]-=1
            t[b]+=1
        for i in range(1, n+1):
            if n-1 == t[i]:
                return i
        return -1