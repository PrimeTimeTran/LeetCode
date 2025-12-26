class Solution(object):
    def lemonadeChange(self, bills):
        n5 = n10 = 0
        for b in bills:
            if b == 5:
                n5 += 1
            elif b == 10:
                if n5 > 0:
                    n10 += 1
                    n5 -= 1
                else:
                    return False
            else:
                if n10 > 0 and n5 > 0:
                    n10 -= 1
                    n5 -= 1
                elif n5 > 2:
                    n5 -= 3
                else:
                    return False
        return True

