class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(set)
        for u, v in roads:                            # convert edge data to
            graph[u].add(v), graph[v].add(u)          # the adjacency map
            
        def dfs(n, dst):                              # this function accumulates total cost paid
            ppl, ltr = 1, 0                           # by all people coming from a given city
            
            for src in graph[n]:                      # [1] recursively query each neighbour
                if src == dst : continue              #     city (except for the destination)
                p, l = dfs(src, n)                  
                ppl += p                              # [2] accumulate people from each subtree...
                ltr += l                              #     ...and total cost paid (in liters)
            ltr += (ppl - 1) // seats + 1             # [3] add liters equal to the number of cars 
            return ppl, ltr                           #     needed to go to the next city
            
        return sum(dfs(n,0)[1] for n in graph[0])     # [4] sum liters for all capital's neighbours