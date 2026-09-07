class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = math.prod(nums)
        output = []

        for i, n in enumerate(nums):
            if n == 0:
                i_element = math.prod(nums[:i]) * math.prod(nums[i+1:])
                output = [0] * i + [i_element] + [0] * (len(nums) - i - 1)
                return output

            output.append(full_product // n)

        return output