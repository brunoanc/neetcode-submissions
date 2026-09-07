class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        string_start = 0
        string_end = 0
        max_len = 0

        current_max_freq = 1

        char_counts = {}

        while string_end < len(s):
            c = s[string_end]

            char_counts[c] = char_counts.get(c, 0) + 1

            if char_counts[c] > current_max_freq:
                current_max_freq = char_counts[c]

            while (string_end - string_start + 1) - current_max_freq > k:
                char_counts[s[string_start]] -= 1
                string_start += 1

            if (string_end - string_start + 1) > max_len:
                max_len = string_end - string_start + 1

            string_end += 1

        return max_len