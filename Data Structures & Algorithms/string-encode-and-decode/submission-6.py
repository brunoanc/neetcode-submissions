class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        return "ñ".join(strs) + "ñ"

    def decode(self, s: str) -> List[str]:
        strs = []

        if len(s) == 0:
            return strs

        current_str = ""

        for c in s:
            if c != "ñ":
                current_str += c
                continue

            strs.append(current_str)
            current_str = ""

        return strs