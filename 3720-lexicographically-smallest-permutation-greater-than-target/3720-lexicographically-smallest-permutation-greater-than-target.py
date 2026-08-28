
class Solution:
  def lexGreaterPermutation(self, s: str, target: str) -> str:
    counts = Counter(s)
    for i in range(len(target) - 1, -1, -1):
      prefix_counts = Counter(target[:i])
      if any(prefix_counts[c] > counts[c] for c in prefix_counts):
        continue
      remaining = counts - prefix_counts
      bigger = [c for c in remaining if c > target[i]]
      if bigger:
        c = min(bigger)
        remaining[c] -= 1
        if remaining[c] == 0:
          del remaining[c]
        suffix = []
        for char in sorted(remaining):
          suffix.append(char * remaining[char])
        return target[:i] + c + "".join(suffix)
    return ""
