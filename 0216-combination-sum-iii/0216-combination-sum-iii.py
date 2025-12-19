'''
1. Understand
2. Diagram
3. Pseudocode
4. Code
5. BigO
Time:    O(2⁹⋅k)    ⇒ O(1) 
k is the length of the path which sums to n. Because the constraints says it's bound by a constant number, 9, it's constant.
Space:   O(k)       ⇒ O(1)
k is the length of the path which sums to n. Because the constraints says it's bound by a constant number, 9, it's constant.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def back(start, path):
            if len(path) == k and sum(path) == n:
                return res.append(path)
            for i in range(start, 10):
                back(i+1, path+[i])
            return res
        return back(1, [])