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
        print(s)

        while True:
            if i >= len(s):
                break

            count = ""

            for c in s[i:]:
                if c == "#":
                    break

                count += c

            #print(count, i, strs)
            count_int = int(count)
            strs.append(s[i+1+len(count):i+1+len(count)+count_int])
            i += (count_int + 1 + len(count))

        return strs