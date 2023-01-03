'''

3. Pseudocode

- Create a graph using edges 
- Traverse graph using bfs starting at node k. 
- Check if the node has been seen, if so continue
- Add node to seen nodes
- Check if the length of seen nodes is equal to number of nodes, if so break
- Add neighbors of node to queue adding current time taken
- Return time if number of nodes seen equal to number of nodes, else return -1


'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u,v,w in times:
            g[u].append((v,w))
            
        seen = set()
        q = [(0,k)]
        
        while q: 
            time, u = heapq.heappop(q)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: break
            for v, nt in g[u]:
                heapq.heappush(q, (time+nt, v))
        
        return time if len(seen) == n else -1
        