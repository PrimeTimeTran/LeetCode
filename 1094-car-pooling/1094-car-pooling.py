class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur, events = 0, []
        for n, start, end in trips:
            events.append([start, n])
            events.append([end, -n])
        events.sort()
        for _, delta in events:
            cur += delta
            if cur > capacity:
                return False
        return True