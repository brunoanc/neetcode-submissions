class Solution:
    def construct_key(self, string: str):
        counts = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}

        for c in string:
            counts[c] = counts[c] + 1

        return tuple(counts.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for i, str_1 in enumerate(strs):
            key = self.construct_key(str_1)
            anagrams[key] = anagrams.get(key, []) + [str_1]

        return list(anagrams.values())
