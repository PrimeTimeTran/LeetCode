class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ = deque()
        dQ = deque()
        
        for i,c in enumerate(senate):
            if c == "R":
                rQ.append(i)
            else:
                dQ.append(i)
        while dQ and rQ:
            d,r = dQ.popleft(), rQ.popleft()
            
            if d < r:
                dQ.append(d+len(senate))
            else:
                rQ.append(r+len(senate))
        return "Radiant" if rQ else "Dire"