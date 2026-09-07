class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            l = nums[left]
            r = nums[right]
            m = nums[middle]

            # Check if we are right there
            if nums[middle - 1] > m:
                return m
            if m > r:
                left = middle + 1
                # r in correct section
            else:
                right = middle
                # l, m in right side

        return nums[left]