class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = list()

        anagrams = dict()

        for i, str_1 in enumerate(strs):
            sorted_1 = "".join(sorted(str_1))
            anagrams[sorted_1] = anagrams.get(sorted_1, []) + [str_1]

        return list(anagrams.values())
