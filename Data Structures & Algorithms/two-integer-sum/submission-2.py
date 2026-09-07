class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements[nums[i]], i]

            complements[target - nums[i]] = i
