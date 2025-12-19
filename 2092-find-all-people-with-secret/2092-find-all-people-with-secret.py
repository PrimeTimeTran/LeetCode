'''
1. Understand
Correct strategy (high-level)
Sort meetings by time
Process meetings grouped by the same time
For each time group:
- Union all participants in that time
- Check which connected components contain someone who knows the secret
- Only keep those unions
- Reset the rest
This preserves simultaneity correctly.
2. Diagram
3. Pseudocode
4. Code
5. BigO
   Time: O()
   Space: O()
'''
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Person 0 and firstPerson know the secret initially
        union(0, firstPerson)

        meetings.sort(key=lambda x: x[2])
        i = 0

        while i < len(meetings):
            time = meetings[i][2]
            people = set()

            # union all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                people.add(x)
                people.add(y)
                i += 1

            # keep only components connected to 0
            for p in people:
                if find(p) != find(0):
                    parent[p] = p  # reset

        return [i for i in range(n) if find(i) == find(0)]
