from typing import List

class Solution:
    def is_valid_code(self, s: str) -> bool:
        return all(ch.isalnum() or ch == '_' for ch in s) and len(s) > 0

    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:
        cats = ['electronics', 'grocery', 'pharmacy', 'restaurant']
        order = {cat: i for i, cat in enumerate(cats)}

        valid = []

        for c, b, a in zip(code, businessLine, isActive):
            if self.is_valid_code(c) and b in order and a:
                valid.append((order[b], c))

        valid.sort(key=lambda x: (x[0], x[1]))

        return [c for _, c in valid]
