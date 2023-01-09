class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        print(tickets)
        print(sorted(tickets))
        print(sorted(tickets)[::-1])
        for a, b in sorted(tickets)[::-1]:
            g[a].append(b)
        
        route = []
        def visit(airport):
            while g[airport]:
                visit(g[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
