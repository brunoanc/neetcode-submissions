class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        parentheses = []

        for c in s:
            if c in parentheses_dict:
                if len(parentheses) == 0:
                    return False

                if parentheses[-1] == parentheses_dict[c]:
                    parentheses.pop()
                else:
                    return False
            else:
                parentheses.append(c)

        return len(parentheses) == 0
