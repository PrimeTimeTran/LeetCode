'''
1. Understand
We are scheduling meetings into rooms. Each meeting has a start and end time.
If a room is free at the meeting’s start, we assign the meeting to the smallest-
indexed available room. If no room is free, we delay the meeting until the
earliest room becomes available.

We must count how many meetings each room handles and return the room with
the highest count (ties broken by smaller index).

2. Strategy
Greedy + Heaps.

We maintain:
- `ready`: a min-heap of room indices that are currently free
- `rooms`: a min-heap of (endTime, roomIndex) for rooms currently in use

Meetings are processed in ascending start-time order.

3. Greedy Choice Property
At each meeting:
- If rooms are free, assigning the meeting to the smallest-index available room
  is optimal and required by the problem.
- If no room is free, delaying the meeting to the earliest-ending room causes
  the least possible delay and preserves feasibility for future meetings.

This local choice minimizes wasted time and ensures correctness globally.

4. Optimal Substructure
Once a meeting is assigned to a room (possibly delayed), the remaining problem
is identical:
- with updated room availability times
- and the remaining meetings

The optimal schedule of the remaining meetings depends only on this updated
state, not on how earlier meetings were assigned.

5. Big O
Let m = number of meetings, n = number of rooms

Sorting meetings:        O(m log m)

For each meeting:
- Heap pops/pushes:      O(log n)

Total Time:              O(m log m + m log n)
                         = O(m log m) (since m ≥ n)

Space:
- `ready` heap:          O(n)
- `rooms` heap:          O(n)
- result array:          O(n)

Total Space:             O(n)
'''

class Solution:
    def mostBooked(self, n, meetings):
        occupied, vacant = [], [r for r in range(n)]
        utilization = [0] * n
        heapify(vacant)
        for start, end in sorted(meetings):
            while occupied and occupied[0][0] <= start:
                _, r = heappop(occupied)
                heappush(vacant, r)
            if vacant:
                r = heappop(vacant)
                heappush(occupied, [end, r])
            else:
                end_time, r = heappop(occupied)
                heappush(occupied, [end_time + end - start, r])
            utilization[r] += 1
        return utilization.index(max(utilization))