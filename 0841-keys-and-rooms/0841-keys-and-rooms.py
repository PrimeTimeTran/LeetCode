class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        def dfs(r):
            if r in seen:
                return
            seen.add(r)
            for room in rooms[r]:
                if room not in seen:
                    dfs(room)
        
        dfs(0)
        return len(seen) == len(rooms)