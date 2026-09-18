class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        
        for i in range(n):
            char = s[i]
            if i != first[char]:
                continue  
                
            right = last[char]
            valid = True
            j = i
            
            while j <= right:
                c = s[j]
                if first[c] < i:
                    valid = False
                    break
                right = max(right, last[c])
                j += 1
                
            if valid:
                intervals.append((i, right))
                
        intervals.sort(key=lambda x: x[1])
        
        selected = []
        last_end = -1
        
        for l, r in intervals:
            if l > last_end:
                selected.append((l, r))
                last_end = r
                
        return [s[l:r+1] for l, r in selected]