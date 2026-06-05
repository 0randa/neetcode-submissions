class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        numItems = len(heights)


        max_area = 0

        for i in range(numItems):
            for j in range(i, numItems):
                height = min(heights[i], heights[j])
                width = j - i

                max_area = max(max_area, height * width)


        return max_area