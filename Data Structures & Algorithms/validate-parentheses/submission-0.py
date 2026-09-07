class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        parentheses = []

        for c in s:
            if len(parentheses) != 0 and c in parentheses_dict and parentheses[-1] == parentheses_dict[c]:
                parentheses.pop()
            else:
                parentheses.append(c)

        return len(parentheses) == 0
