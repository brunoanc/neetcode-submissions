class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_dict = {}

        for n in nums:
            number_dict[n] = 1

        longest = 0

        for n in nums:
            if n not in number_dict:
                continue

            chain = 0
            k = n

            while k in number_dict:
                del number_dict[k]
                chain += 1
                k += 1

            k = n - 1

            while k in number_dict:
                del number_dict[k]
                chain += 1
                k -= 1

            if chain > longest:
                longest = chain

            if longest == len(nums):
                break

        return longest
