def merge(a,b):
    c,i,j = [], 0, 0
    while i<len(a) or j<len(b):
        if i==len(a) or (j<len(b) and a[i]>b[j]):
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
    return c
def gensub(mask):
    res = (mask-1)&mask
    while res:
        yield res
        res = (res-1) & mask

class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        data = [[] for _ in range(1<<n)]
        for i,l in enumerate(lists): data[1<<i] = l
        costs = [math.inf]*len(data)
        for i in range(1, len(data)):
            if len(data[i])>0: continue
            j=i&-i
            k=i-j
            data[i] = merge(data[j], data[k])
        median=[0]*len(data)
        for i in range(1, len(data)):
            median[i] = data[i][(len(data[i])-1)//2]
        for i in range(n):
            costs[1<<i] = 0
        costs[0]=0
        for mask in range(1, len(data)):
            for x in gensub(mask):
                y = mask-x
                if x<y: break
                costs[mask] = min(costs[mask], costs[x] + costs[y] + len(data[x]) + len(data[y]) + abs(median[x]-median[y]))
        return costs[-1]
            

        

        