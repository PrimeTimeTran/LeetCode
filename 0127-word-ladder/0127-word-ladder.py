'''
Create g with wildcard keys containing their variants.
BFS from start looking for word matching end.

'''
class Solution:
    def ladderLength(self, s: str, e: str, words: List[str]) -> int:
        g = defaultdict(list)
        
        for w in words:
            for j in range(len(w)):
                pat = w[:j] + '*' + w[j+1:]
                g[pat].append(w)
        res = 1
        seen = set()        
        q = deque([s])
        while q: 
            for _ in range(len(q)):
                w = q.popleft()
                if w == e: return res
                for j in range(len(w)):
                    pat = w[:j] + '*' + w[j+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            
            res+=1
        return 0