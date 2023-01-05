'''
Create graph/adj list/hm of wildcarded words with matches
Use BFS to search graph. Start from begin word in graph to neighbor's adding non seen words to q.
For every word wildcard varient, increment res.


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
    def ladderLength(self, start: str, end: str, words: List[str]) -> int:
        g = defaultdict(list)

        for w in words:
            for j in range(len(w)):
                pat = w[:j] + '*' + w[j+1:]
                g[pat].append(w)

        res = 1
        q = deque([start])
        seen = set(start)
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == end:
                    return res
                for j in range(len(w)):
                    pat = w[:j] + '*' + w[j+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        return 0