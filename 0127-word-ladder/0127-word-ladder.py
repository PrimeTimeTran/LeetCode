'''
Validate input wordList. 
Create graph of wildcarded words with potential matches
Use BFS to search from start to end word. Iterate for every item in q and only add non seen words to q.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        g = defaultdict(list)
        wordList.append(beginWord)
        
        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + "*" + w[j+1:]
                g[pat].append(w)
        q = deque([beginWord])
        seen = set(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pat = w[:j] + "*" + w[j+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        return 0