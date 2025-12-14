'''
1. Understand
Ascertain if the strings are anagrams of one another.
Anagrams are strings that contain the same number of every character. In other words one string can be rearranged to form the other string.

2. Diagram
    1. Compare Counters of each string being the same.
    2. Count number of each unique character in each string, then compare the counts of all chars in both counters and return false if they don't match
3. Pseudocode
    Iterate chars of each string counting the number of occurances of each unique char.
    Next loop dict of chars created and compare one dict's value to the other. 
    If they don't match, return false.
    If we loop the dicts and all chars match in value, then return true.
4. Code
5. BigO

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sStore, tStore = {}, {}
        for c in s:
            sStore[c] = 1 + sStore.get(c, 0)
        for c in t:
            tStore[c] = 1 + tStore.get(c, 0)
        if len(tStore) != len(sStore):
            return False
        for k, v in sStore.items():
            if k not in tStore or tStore[k] != v:
                return False
        return True