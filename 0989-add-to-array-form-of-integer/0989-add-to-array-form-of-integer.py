class Solution:
    def addToArrayForm(self, a: List[int], k: int) -> List[int]:
        s = ''
        for n in a:
            s += str(n)
            
        arr = []
        for n in str(int(s)+ k):
            arr.append(int(n))
        print(arr)
        return arr