class Solution:
    def construct_key(self, string: str):
        counts = [0] * 26

        for c in string:
            counts[ord(c) - ord("a")] += 1

        return tuple(counts)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for string in strs:
            key = self.construct_key(string)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        return list(anagrams.values())
