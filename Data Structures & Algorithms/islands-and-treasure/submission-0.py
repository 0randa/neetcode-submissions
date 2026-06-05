class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid) , len(grid[0])
        INF = 2147483647 
        new_output =  [[[-1 for _ in range(ROWS)] for _ in range(COLS)]]

        def dfs(r,c,visited):
            nonlocal distance
            if r < 0 or r >=ROWS or c < 0 or c>= COLS or (r,c) in visited or grid[r][c] == -1:
                return

            if grid[r][c] == 0:
                distance = len(visited)
                return

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dx, dy in directions:
                visited.add((r + dx,c + dy))
                dfs(r+dx, c+dy, visited)

        for r in range(ROWS):
            for c in range(COLS):
                distance = INF
                dfs(r,c, set())
                new_output[r][c] = distance

        return new_output


