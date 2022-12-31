'''
1. Constraints

Return array/list


2. Pseudocode

Create an g/adj list using pre

Iterate over each course and if we encounter a cycle, return an empty array.
    - Check if course seen, if so check if course taken
    - Loop over the courses' pre
    - Add course to res

We return our list

'''

class Solution:
    def findOrder(self, N: int, pre: List[List[int]]) -> List[int]:
        g = {c:[] for c in range(N)}
        for a,b in pre:
            g[a].append(b)
        res = []
        seen = {}
        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = False
            for p in g[c]:
                if not dfs(p): return False
            seen[c] = True
            res.append(c)
            return True
        
        for c in range(N):
            if not dfs(c): return []
        return res        
        
        return res