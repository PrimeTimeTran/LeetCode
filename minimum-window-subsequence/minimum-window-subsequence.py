
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n,m=len(S),len(T)
        i=0
        L,R=-1,math.inf
        while i<n:
            j=0
            while i<n and j<m:
                if S[i]==T[j]:
                    j+=1
                i+=1
            if j<m:
                break
            tmpi=i-1
            j=m-1
            while j>=0:
                if S[tmpi]==T[j]:
                    j-=1
                tmpi-=1
            if i-tmpi-1<R:
                R=i-tmpi-1
                L=tmpi+1
            i=tmpi+2
        return '' if L<0 else S[L:L+R]