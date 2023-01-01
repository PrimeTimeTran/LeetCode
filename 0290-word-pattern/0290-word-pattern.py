class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words): return False
        map = {}
        for l, word in zip(pattern, words):
            if l not in map:
                if word in map.values(): return False
                map[l] = word
            else: 
                if map[l] != word: return False
        return True