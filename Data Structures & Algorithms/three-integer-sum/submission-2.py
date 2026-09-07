class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        for i, n in enumerate(nums):
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

                    if triplet not in triplets:
                        triplets.append(triplet)

        return triplets