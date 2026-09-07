class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        initial_index = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in seen and seen[c] >= initial_index:
                initial_index = seen[c] + 1

            seen[c] = i
            length = i - initial_index + 1

            if length > max_len:
                max_len = length

        return max_len