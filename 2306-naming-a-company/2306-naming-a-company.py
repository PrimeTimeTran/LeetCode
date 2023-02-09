class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = defaultdict(set)
        for a in ideas:
            count[a[0]].add(hash(a[1:]))
        res = 0
        for a, seta in count.items():
            for b, setb in count.items():
                if a >= b: continue
                same = len(seta & setb)
                res += (len(seta) - same) * (len(setb) - same)
        return res * 2
    
        r = list(permutations(ideas, 2))
        res = []
        for a,b in r:
            a,b = list(a), list(b)
            a[0], b[0] = b[0], a[0]
            a = ''.join
            (a)
            b = ''.join(b)
            if a not in ideas and b not in ideas:
                res.append(a + ' ' + b)
        print(list(set(res)))
        return len(list(set(res)))
                             