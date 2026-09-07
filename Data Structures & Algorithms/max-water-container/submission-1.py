class Solution:
    def calculateArea(self, i: int, j: int, heights: List[int]) -> int:
        width = abs(i - j)
        height = min(heights[i], heights[j])
        return width * height

    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            area = self.calculateArea(i, j, heights)

            if area > max_area:
                max_area = area

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area