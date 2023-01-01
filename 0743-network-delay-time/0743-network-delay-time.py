'''
1. Constraints
We receive an array of weighted edges. We also receive a start node, k and a variable n for number of nodes.

We should return an integer

2. Diagram

3. Pseudocode

Use a pq to track nodes we need to visit and the time so far.
Iterate through all nodes until we've visited all nodes.
If the number of nodes visited is the same as n return our time, otherwise return -1


'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v, w))
        
        seen = set()
        heap = [(0, k)]

        while heap:
            t, u = heapq.heappop(heap)
            # t, u = heap.pop(0)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heapq.heappush(heap, (t+nt, v))
                # heap.append((t+nt, v))
                
        
        
        return t if len(seen) == n else -1