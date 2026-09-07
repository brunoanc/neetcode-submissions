class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set()

        for n in nums:
            number_set.add(n)

        longest = 0

        for n in nums:
            if n not in number_set:
                continue

            chain = 0
            k = n

            while k in number_set:
                number_set.remove(k)
                chain += 1
                k += 1

            k = n - 1

            while k in number_set:
                number_set.remove(k)
                chain += 1
                k -= 1

            if chain > longest:
                longest = chain

            if longest == len(nums):
                break

        return longest
