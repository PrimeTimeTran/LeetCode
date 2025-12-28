class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g, q, seen = defaultdict(list), [[0,k]], set()
        for u,v,w in times: g[u].append([v,w])
        while q:
            accum_time, u = heappop(q)
            if u in seen: continue
            seen.add(u)
            if len(seen) == n: return accum_time
            for des, time in g[u]:
                heappush(q, [time + accum_time, des])
        return -1