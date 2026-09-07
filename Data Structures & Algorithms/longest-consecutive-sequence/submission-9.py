class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0

        for n in number_set:
            if n - 1 in number_set:
                continue

            chain = 0
            k = n

            while k in number_set:
                chain += 1
                k += 1

            longest = max(longest, chain)

        return longest
