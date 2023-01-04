class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g = defaultdict(set)
        for word in wordList:
            if word != beginWord:
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    g[pat].add(word)
        q = deque([beginWord])
        visited = {beginWord: 1}
        parent_list = defaultdict(set)
        ans_path = []

        while q:
            word = q.popleft()
            if word == endWord: break
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                for next_word in g[pat]:
                    if next_word not in visited:
                        visited[next_word] = visited[word] + 1
                        q.append(next_word)
                        parent_list[next_word].add(word)
                    elif visited[next_word] > visited[word]:
                        parent_list[next_word].add(word)
        print(visited)
        def dfs(word, path):
            if word == beginWord:
                ans_path.append(path[::-1])
            for next_word in parent_list[word]:
                dfs(next_word, path+[next_word])
        
        dfs(endWord, [endWord])
        return ans_path