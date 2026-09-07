class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = dict()

        for a, b in zip(s, t):
            chars[a] = chars.get(a, 0) + 1
            chars[b] = chars.get(b, 0) - 1

        return all(n == 0 for n in chars.values())

