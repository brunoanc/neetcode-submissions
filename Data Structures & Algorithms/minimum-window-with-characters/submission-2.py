class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars = {}
        missing_char_count = len(set(t))

        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        shortest_sub_start = -1
        shortest_sub_end = -1

        sub_start = 0
        sub_end = 0

        while sub_end < len(s):
            c = s[sub_end]

            if c in t_chars:
                t_chars[c] -= 1

                if t_chars[c] == 0:
                    missing_char_count -= 1

            while missing_char_count == 0:
                if shortest_sub_end == -1 or sub_end - sub_start + 1 < shortest_sub_end - shortest_sub_start + 1:
                    shortest_sub_end = sub_end
                    shortest_sub_start = sub_start

                c_start = s[sub_start]

                if c_start in t_chars:
                    t_chars[c_start] += 1

                    if t_chars[c_start] == 1:
                        missing_char_count += 1

                sub_start += 1

            sub_end += 1

        return s[shortest_sub_start:shortest_sub_end + 1]
