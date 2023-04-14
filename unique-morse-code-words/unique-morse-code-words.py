import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
		"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = string.ascii_lowercase
        hashmap = {alpha[i]: morse[i] for i in range(len(alpha))}
        hashset = set()
        for word in set(words):
            t = "" # transform
            for ch in word:
                t += hashmap[ch]
            hashset.add(t)
        return len(hashset)