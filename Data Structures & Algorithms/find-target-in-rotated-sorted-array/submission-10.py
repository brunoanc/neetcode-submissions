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

        if pivot == 0:
            l = 0
            r = len(nums) - 1
        elif nums[0] <= target <= nums[pivot - 1]:
            l = 0
            r = pivot - 1
        else:
            l = pivot
            r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1