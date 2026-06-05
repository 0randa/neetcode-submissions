class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        # add all the treasure chests to the queue

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))


        def add_room(r,c,value, queue):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
            grid[r][c] != INF):
                return
            queue.append((r,c))
            grid[r][c] = value + 1
            
        while q:
            r, c = q.popleft()

            # check all neighbours
            add_room(r + 1,c,grid[r][c], q)
            add_room(r - 1,c,grid[r][c], q)
            add_room(r,c + 1,grid[r][c], q)
            add_room(r,c - 1,grid[r][c], q)



