from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)

        # A palindrome can have at most one odd-frequency character.
        odd = [c for c, n in freq.items() if n % 2]

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Counts for the left half.
        half = Counter({
            c: n // 2
            for c, n in freq.items()
            if n // 2 > 0
        })

        half_len = len(s) // 2
        target_left = target[:half_len]

        def make_palindrome(left):
            return left + middle + left[::-1]

        def smallest_greater(counts, bound):
            """
            Find the smallest permutation of `counts`
            that is strictly greater than `bound`.
            """

            # We first try to follow bound as long as possible.
            path = []

            def dfs(pos, greater):
                if pos == half_len:
                    if greater:
                        return "".join(path)
                    return None

                if greater:
                    # Once we're greater, greedily use the smallest
                    # available character for the rest.
                    remaining = []
                    for c in sorted(counts):
                        remaining.extend([c] * counts[c])

                    return "".join(path) + "".join(remaining)

                # Try characters in increasing order.
                for c in sorted(counts):
                    if counts[c] == 0:
                        continue

                    # Can't use a character that would make us smaller.
                    if c < bound[pos]:
                        continue

                    counts[c] -= 1
                    path.append(c)

                    result = dfs(
                        pos + 1,
                        c > bound[pos]
                    )

                    if result is not None:
                        return result

                    path.pop()
                    counts[c] += 1

                return None

            return dfs(0, False)

        # First find the smallest left half >= target_left.
        def smallest_at_least(counts, bound):
            path = []

            def dfs(pos, greater):
                if pos == half_len:
                    return "".join(path)

                for c in sorted(counts):
                    if counts[c] == 0:
                        continue

                    if not greater and c < bound[pos]:
                        continue

                    counts[c] -= 1
                    path.append(c)

                    result = dfs(
                        pos + 1,
                        greater or c > bound[pos]
                    )

                    if result is not None:
                        return result

                    path.pop()
                    counts[c] += 1

                return None

            return dfs(0, False)

        left = smallest_at_least(half.copy(), target_left)

        if left is None:
            return ""

        candidate = make_palindrome(left)

        if candidate > target:
            return candidate

        # We got exactly target's left half, but its palindrome
        # wasn't greater than target. Get the next left-half permutation.
        left = smallest_greater(half.copy(), target_left)

        if left is None:
            return ""

        return make_palindrome(left)