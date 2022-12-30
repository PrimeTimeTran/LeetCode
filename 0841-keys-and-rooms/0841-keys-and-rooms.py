'''
1. Constraints
We receive a list, we return a boolean


2. Diagram

3. Pseudocode

4. Code
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set([0])
        
        def dfs(k):
            if k in visit:
                return
            visit.add(k)
            
            for key in rooms[k]:
                dfs(key)
            
        for key in rooms[0]:
            if key not in visit:
                dfs(key)
        
        return len(visit) == len(rooms)