'''
if s1 == s2:
    return True  # if strings are equal then swaping is not required
if sorted(s1) != sorted(s2):
    return False    # if sorted s1 and s2 are not equal then swaping will not make strings equal

count = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        count +=1  
if count != 2: # the count should be 2, then only we can do at most one string swap
    return False

return True
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        a, b = Counter(s1), Counter(s2)
        
        if not a == b:
            return False
        
        c = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c+=1
        if c != 2:
            return False
        return True