class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        MAX_ROWS, MAX_COLS = len(grid), len(grid[0])

        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        # add all neighbours
        while fresh > 0 and q:
            len_q = len(q)

            for i in range(len_q):

                (r, c) = q.popleft()

                for dx, dy in directions:

                    row, col = r + dx, c + dy

                    if (row < 0 or col < 0 or row >= MAX_ROWS or col >= MAX_COLS or grid[row][col] != 1):
                        continue

                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1