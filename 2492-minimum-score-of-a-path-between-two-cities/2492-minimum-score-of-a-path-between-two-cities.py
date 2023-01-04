'''
DFS: 
From node one traverse through neighbors using adj list comparing roads to find the minimum score road.
Guard against cycles by checking if road seen with a set.

BFS: 


'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))

        res = inf
        seen = set()
        q = deque([1])
        
        while q:
            n = q.popleft()
            for nei, d in g[n]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(n)
                res = min(res, d)
        return res