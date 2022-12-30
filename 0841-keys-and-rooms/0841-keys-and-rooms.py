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
        
        def dfs(r):
            for key in rooms[r]:
                if key not in visit:
                    visit.add(key)
                    dfs(key)
            
        dfs(0)
        
        return len(visit) == len(rooms)