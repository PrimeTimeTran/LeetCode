'''
Create wildcard keys with matching potential values as adj list.
Use BFS to with nested for loop to work though layer, count number of layers.

'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        
        for w in wordList:
            for i in range(len(w)):
                pat = w[:i] + '*' + w[i+1:]
                g[pat].append(w)
        
        t = 1
        q = deque([beginWord])
        seen = set([beginWord])
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord: 
                    return t
                for i in range(len(w)):
                    pat = w[:i] + '*' + w[i+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
                
            t+=1
        
        
        return 0 