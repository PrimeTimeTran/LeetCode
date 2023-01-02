
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ### UF is a hash map where you can find the root of a group of elements giving an element.
        ### A key in UF is a element, UF[x] is x's parent.
        ### If UF[x] == x meaning x is the root of its group.
        UF = {}
        
        ### Given an element, find the root of the group to which this element belongs.
        def find(x):
            ### this may be the first time we see x, so set itself as the root.
            if x not in UF:
                UF[x] = x
            ### If x == UF[x], meaning x is the root of this group.
            ### If x != UF[x], we use the find function again on x's parent UF[x] 
            ### until we find the root and set it as the parent (value) of x in UF.
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        ### Given two elements x and y, we know that x and y should be in the same group, 
        ### this means the group that contains x and the group that contains y 
        ### should be merged together if they are currently separate groups.
        ### So we first find the root of x and the root of y using the find function.
        ### We then set the root of y (rootY) as the root of the root of x (rootX).
        def union(x, y):
            
            rootX = find(x)
            rootY = find(y)
            # set the root of y (rootY) as the root of the root of x (rootX)
            UF[rootX] = rootY
        
        ### Connect nodes together if there is an edge
        for s,e in edges:
            union(s,e)
        
        ### If the root of source and destination are the same, they are connected somehow (i.e., There is a valid path).
        return find(source) == find(destination)
    
        g = {i:[] for i in range(n)}
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        seen = set()
        
        def dfs(nei):
            if nei in seen:
                return False
            if nei == destination:
                return True
            seen.add(nei)
            for neighbor in g[nei]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(source)
    
    