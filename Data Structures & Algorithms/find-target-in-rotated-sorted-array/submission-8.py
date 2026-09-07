class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        offset = 0

        if pivot != 0:
            if nums[0] <= target <= nums[pivot - 1]:
                nums = nums[:pivot]
            else:
                nums = nums[pivot:]
                offset = pivot

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m + offset
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1