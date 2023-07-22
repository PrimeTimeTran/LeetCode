class Solution:
    def parseTernary(self, expression: str) -> str:
        return self._eval(expression, 0)[0]

    def _eval(self, expr: str, start: int) -> tuple[str, int]:
        if start == len(expr) - 1 or expr[start + 1] == ":":
            return expr[start], start
        true = self._eval(expr, start + 2)
        false = self._eval(expr, true[1] + 2)
        return (true[0], false[1]) if expr[start] == "T" else false