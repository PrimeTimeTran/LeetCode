class Solution:
    def countDigitOne(self, n: int) -> int:
        res, pos = 0, 1
        while pos <= n:
            # Split the number into three parts relative to this position
            #
            # Example: n = 824883294, pos = 1000
            #
            #   higher   = 824883
            #   current  = 2
            #   lower    = 294
            #
            higher = n // (pos * 10)
            current = (n // pos) % 10
            lower = n % pos

            # Now count how many times '1' appears at THIS position
            #
            # Case 1: current digit == 0
            #   The '1' cycles are fully determined by higher digits
            #
            if current == 0:
                res += higher * pos

            # Case 2: current digit == 1
            #   Includes:
            #   - all full cycles from higher digits
            #   - plus the remainder from lower digits
            #
            elif current == 1:
                res += higher * pos + (lower + 1)

            # Case 3: current digit > 1
            #   This position fully contributes an extra block of size 'pos'
            #
            else:
                res += (higher + 1) * pos

            # Move to the next digit position
            pos *= 10
        return res