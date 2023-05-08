class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        d = defaultdict(dict)
        for i, row in enumerate(B):
            for j, col in enumerate(row):
                if col!=0:
                    d[j][i]= col
                
        #print(d) // you may use this to get the idea
        row = len(A)
        col = len(B[0])
        res = [[0 for j in range(col)] for i in range(row)]
        
        for i,row in enumerate(A):
            for j in range(col):
                tmp = 0
                for ele in d[j]:
                    tmp+=(d[j][ele]*row[ele])
                res[i][j]=tmp
            
        return res