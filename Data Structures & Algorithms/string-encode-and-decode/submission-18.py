class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))
            encoded_str += "#"
            encoded_str += s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while True:
            if i >= len(s):
                break

            for j in range(i, len(s)):
                if s[j] == "#":
                    break

            count = int(s[i:j])
            start = j + 1
            end = j + 1 + count

            strs.append(s[start:end])
            i = end

        return strs