class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def is_connected(a,b):
            x1, y1, r1 = bombs[a]
            x2, y2, r2 = bombs[b]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return dist <= r1


        conn = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    if is_connected(i,j):
                        conn[i].append(j)

        # 1. BFS
        # q = collections.deque()
        # maxCount = float('-inf')

        # for node in range(len(bombs)):
        #     if conn[node]:
        #         q.append(node)
        #         visited = set()
        #         visited.add(node)
        #         count = 0
        #         while q:
        #             curr = q.popleft()
        #             count+=1
        #             maxCount = max(maxCount, count)
        #             for child in conn[curr]:
        #                 if child not in visited:
        #                     visited.add(child)
        #                     q.append(child)

        # return maxCount if maxCount != float('-inf') else 1


        # 2. DFS

        # stack = []
        # maxCount = float('-inf')

        # for node in range(len(bombs)):
        #     if conn[node]:
        #         visited = set()
        #         stack.append(node)
        #         visited.add(node)
        #         count = 0
        #         while stack:

        #             curr = stack.pop()
        #             count+=1
        #             maxCount = max(maxCount, count)

        #             for child in conn[curr]:
        #                 if child not in visited:
        #                     visited.add(child)
        #                     stack.append(child)
        # return maxCount if maxCount != float('-inf') else 1


        # 3. DFS recursive                
                    
        def dfs(node):

            if node in visited:
                return 0

            visited.add(node)
            
            ans = 1

            if node in conn:
                for child in conn[node]:
                    if child in visited:
                        continue
                    ans += dfs(child)
            
            return ans 

        maxCount = 1
        for node in conn:
            visited = set()
            maxCount = max(maxCount, dfs(node))
        return maxCount