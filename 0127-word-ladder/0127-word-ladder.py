'''
Create graph/adj list/hm of wildcarded words with matches
Use BFS to search from start to end word. Iterate for every item in q and only add non seen words to q.



{
    *ot: [hot, dot, lot],
    h*t: [hot],
    ho*: [hot],
    d*t: [dot],
    do*: [dot, dog],
    *og: [dog, cog, log],
    d*g: [dog],
    l*t: [lot],
    lo*: [lot, log],
    c*g: [cog],
    co*: [cog],
}

'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        
        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + '*' + w[j+1:]
                g[pat].append(w)
        res = 1
        
        seen = set(beginWord)
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pat = w[:j] + '*' + w[j+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res+=1
        return 0