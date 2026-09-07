class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - n

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    triplet = [n, nums[j], nums[k]]

                    j += 1
                    k -= 1

                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

                    triplets.append(triplet)

        return triplets