class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        
        offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        islands = 0

        def dfs(rowNum, colNum):

            if ((rowNum < 0 or rowNum > numRows - 1 or colNum < 0 or colNum > numCols - 1
            ) or grid[rowNum][colNum] != "1" ):
                return False

            if grid[rowNum][colNum] == "1":
                grid[rowNum][colNum] = "X"

            for x, y in offsets:
                dfs(rowNum + x, colNum + y)

            


        
        for rowNum, row in enumerate(grid):
            for colNum, col in enumerate(row):
                if grid[rowNum][colNum] == "1":
                    dfs(rowNum, colNum)    
                    islands += 1

        return islands