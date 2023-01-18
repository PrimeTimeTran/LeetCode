class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        
        for w in wordList:
            for i in range(len(w)):
                pat = w[:i]+'*'+w[i+1:]
                g[pat].append(w)
        
        seen = set()
        res, q = 1, deque([beginWord])
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord: return res
                for i in range(len(w)):
                    pat = w[:i]+'*'+w[i+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res+=1
        return 0