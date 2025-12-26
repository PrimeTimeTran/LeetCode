class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Step 1: Transform the string
        T = '#'.join('^{}$'.format(s))  # add sentinels
        n = len(T)
        P = [0] * n  # radius array
        C = R = 0    # center and right edge of current rightmost palindrome

        for i in range(1, n-1):
            mirr = 2*C - i  # mirror of i around C

            if i < R:
                P[i] = min(R - i, P[mirr])

            # expand around i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # update center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len)//2  # map back to original string indices
        return s[start: start + max_len]
