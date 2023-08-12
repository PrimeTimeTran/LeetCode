class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l
            while s[r] != '#':
                r+=1
            length = int(s[l:r])
            res.append(s[r+1:r+1+length])
            l = r+1+length
        
        return res
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))