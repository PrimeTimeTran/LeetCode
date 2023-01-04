class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = defaultdict(set)
        for w in wordList:
            for j in range(len(w)):
                pat = w[:j] + "*" + w[j+1:]
                g[pat].add(w)

        q = deque([beginWord])
        seen = {beginWord: 1}
        parent_list = defaultdict(set)

        while q:
            word = q.popleft()
            if word == endWord: break
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                for next_word in g[pat]:
                    if next_word not in seen:
                        seen[next_word] = seen[word] + 1
                        q.append(next_word)
                        parent_list[next_word].add(word)
                    elif seen[next_word] > seen[word]:
                        parent_list[next_word].add(word)

        ans_path = []
        def dfs(word, path):
            if word == beginWord:
                ans_path.append(path[::-1])
            for next_word in parent_list[word]:
                dfs(next_word, path+[next_word])
        
        dfs(endWord, [endWord])
        return ans_path