'''
Create G of wildcard keys and BFS from beginWord. If popped word is endWord, return steps.
For each layer away from begin increment steps by 1. For each word, find it's patterns, and add the associated
neighbors to the Q and mark word as seen.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pat = w[:i]+'*'+w[i+1:]
                g[pat].append(w)
                
        q = deque([beginWord])
        seen = set(beginWord)
        steps = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord: return steps
                for i in range(len(w)):
                    pat = w[:i]+'*'+w[i+1:]
                    for nei in g[pat]:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
            steps+=1
        return 0
        