class Solution:
    def canReach(self, a: List[int], start: int) -> bool:
        # if 0 <= i < len(A) and A[i] >= 0:
        #     J = A[i]
        #     A[i]=-1
        #     return J == 0 or self.canReach(A, i + J) or self.canReach(A, i -J)
        # return False
    
        q = [start] # use bfs       
        while q:
            i = q.pop()
            if a[i]==0: return True
            if a[i]>0:
                move,a[i]= a[i], -1
                if i+move<len(a):
                    q.append(i+move)
                if i-move>=0:
                    q.append(i-move)