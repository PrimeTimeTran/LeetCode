class Solution:
    def minDistance(self, word1, word2,cache ={}):
        if not word1 and not word2:
            return 0
        if not len(word1)   or not len(word2):
            return len(word1) or len(word2)
        if word1[0]==word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        if (word1,word2) not in cache:
            inserted = 1 + self.minDistance(word1,word2[1:])
            deleted  = 1 + self.minDistance(word1[1:],word2)
            replaced = 1 + self.minDistance(word1[1:],word2[1:])
            cache[(word1,word2)]= min(inserted,deleted,replaced)
        return cache[(word1,word2)]