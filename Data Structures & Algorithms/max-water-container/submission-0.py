class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find 2 bars, your height will be the minimum between those 2 bars
        # width will be the distance between those 2 bars
        max_area = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])

                if width * height > max_area:
                    max_area = width * height

        return max_area
