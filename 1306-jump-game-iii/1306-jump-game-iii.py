'''
Create G and BFS from start to all other neighbors searching for 0 using a Q

Index
0  1  2  3  4  5  6

Values
4, 2, 3, 0, 3, 1, 2
               . 


'''
class Solution:
    def canReach(self, a: List[int], start: int) -> bool:
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