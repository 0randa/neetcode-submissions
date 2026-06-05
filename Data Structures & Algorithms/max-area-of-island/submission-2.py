class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        numRows, numCols = len(grid), len(grid[0])

        offset = [(-1, 0), (1,0), (0,1), (0,-1)]

        def dfs(rowNum, colNum):
            if rowNum < 0 or rowNum > numRows - 1 or colNum < 0 or colNum > numCols - 1 or grid[rowNum][colNum] != 1:
                return 0

            if grid[rowNum][colNum] == 1:
                grid[rowNum][colNum] = "X"


                area = 1
                for x,y in offset:
                    area += dfs(rowNum + x, colNum + y)

                return area



        max_area = 0

        for rowNum, row in enumerate(grid):
            for colNum, col in enumerate(row):
                area = 0
                if grid[rowNum][colNum] == 1:
                    blob = dfs(rowNum, colNum)

                    max_area = max(max_area, blob)
                    # print(area)

        return max_area



            