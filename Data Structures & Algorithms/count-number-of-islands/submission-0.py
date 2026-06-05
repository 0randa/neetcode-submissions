class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        res = []

        # use a tuple
        def dfs(r, c, island):
            # out of bounds
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == '0':
                return

            # mark as visited
            grid[r][c] = "0"
            island.append((r, c))
            # traval in all 4 directions
            dfs(r + 1, c, island)
            dfs(r - 1, c, island)
            dfs(r, c + 1, island)
            dfs(r, c - 1, island)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island = []
                    dfs(r, c, island)
                    res.append(island)
        return len(res)