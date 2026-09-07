class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = list()

        for i in range(len(nums)):
            for j in range(len(complements)):
                if nums[i] == complements[j]:
                    return [j, i]

            complements.append(target - nums[i])
