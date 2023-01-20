class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = [0]*(n+1)
        for a,b in trust:
            c[a]-=1
            c[b]+=1
            
        for i in range(1, n+1):
            if n-1 == c[i]:
                return i
        return -1