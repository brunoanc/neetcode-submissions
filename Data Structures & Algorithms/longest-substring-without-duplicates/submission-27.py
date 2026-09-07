class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        initial_index = 0
        max_len = -1

        for i, c in enumerate(s):
            if c in seen and seen[c] >= initial_index:
                length = i - initial_index

                if length > max_len:
                    max_len = length

                initial_index = seen[c] + 1

            seen[c] = i

        # Consider last substring
        length = len(s) - initial_index

        if length > max_len:
            return length

        return max_len