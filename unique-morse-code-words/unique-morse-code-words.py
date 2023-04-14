import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
		"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = string.ascii_lowercase
        hashmap = {alpha[i]: morse[i] for i in range(len(alpha))}
        
		# we make a set for collecting unique/different transformations
        hashset = set()
        for word in set(words):
            t = "" # transform
            for ch in word:
                t += hashmap[ch]
            hashset.add(t)
        
		# in the end we just return the length of hashset, which tells us how many different transformations it has seen
        return len(hashset)