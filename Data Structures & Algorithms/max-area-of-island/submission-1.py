class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = []

        def dfs(r, c, islands):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            islands.append((r,c))


            dfs(r + 1, c, islands)
            dfs(r - 1, c, islands)
            dfs(r, c + 1, islands)
            dfs(r, c - 1, islands)

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    islands = []
                    dfs(i, j, islands)
                    res.append(islands)

        max_len = 0
        for r in res:
            max_len = max(max_len, len(r))

        # return len(max(res, key=len))
        return max_len

        





