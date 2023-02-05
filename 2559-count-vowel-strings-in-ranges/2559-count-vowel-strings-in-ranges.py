class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        A = [0] * (n + 1)
        vowel = 'aeiou'
        ans = []
        for i in range(n):
            A[i + 1] = A[i] + (1 if words[i][0] in vowel and words[i][-1] in vowel else 0)
        for l, r in queries:
            ans.append(A[r + 1] - A[l])
        return ans