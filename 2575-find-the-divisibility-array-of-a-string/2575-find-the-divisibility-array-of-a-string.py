class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        div = []

        for i in range(0, len(word)):
            mod = (mod * 10 + int(word[i])) % m
            div.append(1 if mod % m == 0 else 0)
        return div