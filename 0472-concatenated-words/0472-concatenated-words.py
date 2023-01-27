class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        words_dict = set(words)
        for word in words:
            words_dict.remove(word)
            if self.check(word, words_dict) is True:
                res.append(word)
            words_dict.add(word)
        return res
    
    def check(self, word, d):
        if word in d:
            return True
        
        for i in range(len(word),0, -1):
            if word[:i] in d and self.check(word[i:], d):
                return True
        return False