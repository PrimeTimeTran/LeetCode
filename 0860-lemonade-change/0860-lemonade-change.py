class Solution(object):
    def lemonadeChange(self, bills):
        c5 = c10 = 0
        for b in bills:
            if b == 5:
                c5 += 1
            elif b == 10:
                if c5 > 0:
                    c5 -= 1
                else:
                    return False
                c10 += 1
            else:
                if c10 > 0 and c5 > 0:
                    c10 -= 1
                    c5 -= 1
                elif c5 > 2:
                    c5 -= 3
                else:
                    return False
        return True
