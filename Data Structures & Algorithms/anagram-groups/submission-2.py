class Solution:
    def construct_key(self, string: str):
        counts = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}

        for c in string:
            counts[c] = counts[c] + 1

        return tuple(counts.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for string in strs:
            key = self.construct_key(string)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        return list(anagrams.values())
