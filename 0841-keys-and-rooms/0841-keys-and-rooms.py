class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        def dfs(r):
            if r in seen: return
            seen.add(r)
            for room in rooms[r]:
                dfs(room)
        dfs(0)
        return len(seen) == n