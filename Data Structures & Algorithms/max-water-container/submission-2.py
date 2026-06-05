class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        numItems = len(heights)


        max_area = 0

        def get_height(i, j):
            return min(heights[i], heights[j])

        def get_width(i, j):
            return j - i


        l = 0
    
        for r, height in enumerate(heights):
            
            height = get_height(l, r)
            width = get_width(l, r)
            
            if heights[r] > heights[l]:
                l += 1

            max_area = max(max_area, height * width)





        return max_area