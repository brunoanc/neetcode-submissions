class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        chars = dict()

        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]

            chars[c_s] = chars.get(c_s, 0) + 1
            chars[c_t] = chars.get(c_t, 0) - 1

        for n in chars.values():
            if not n == 0:
                return False

        return True
