class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        map = {}
        for l, word in zip(pattern, s.split(' ')):
            if l not in map:
                if word in map.values(): return False
                map[l] = word
            else: 
                if map[l] != word:
                    return False
                
        return True
                
                