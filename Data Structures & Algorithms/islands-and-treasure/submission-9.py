class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        offsets = [(1,0), (0,1), (-1,0), (0,-1)]
        
        # add all the treasure chests to the queue

        q = deque()
        seen = set()
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 0:
                    q.append((i,j))
                    seen.add((i,j))

        while q:
            for _ in range(len(q)): # iterate through all the current elements
                i, j = q.popleft()

                for dx, dy in offsets:
                    # check that the neighbour is not already visited, and also check that its not a wall, also check that it is within bounds
                    if i + dx < 0 or j + dy < 0 or i + dx >= len(grid) or j + dy >= len(grid[0]) or grid[i+dx][j+dy] == -1 or (i+dx, j+dy) in seen:
                        continue

                    if grid[i+dx][j+dy] == INF:
                        q.append((i+dx, j+dy))
                        seen.add((i+dx, j+dy))
                        grid[i+dx][j+dy] = grid[i][j] + 1
                    




        