class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        s = int(s) + 1
        lst = [int(char) for char in str(s)]
        return lst