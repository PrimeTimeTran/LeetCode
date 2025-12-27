class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for n, f, t in trips:
            events.append([f, n])
            events.append([t, -n])
        events.sort()
        cur = 0
        for _, delta in events:
            cur += delta
            if cur > capacity:
                return False
        return True