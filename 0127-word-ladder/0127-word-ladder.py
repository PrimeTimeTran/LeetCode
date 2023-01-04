'''
Create graph matching each word pattern to it's viable patterns.
Use BFS to search through all words for potential match to endWord.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + '*' + w[j+1:]
                nei[pat].append(w)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pat = word[:j] + '*' + word[j+1:]
                    for nt in nei[pat]:
                        if nt not in visit:
                            visit.add(nt)
                            q.append(nt)
            res+=1
        return 0