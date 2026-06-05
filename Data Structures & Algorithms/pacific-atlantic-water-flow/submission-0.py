class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # first row, first column are pacific
        # last row, last col are atlantic
        PACIFIC_ROW, PACIFIC_COL = 0, 0
        ATLANTIC_ROW, ATLANTIC_COL = len(heights), len(heights[0])

        print(ATLANTIC_COL)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c, visited):
            pacific, atlantic = False, False
            q = deque()
            q.append((r,c))

            while q:
                (row, col) = q.popleft()
                if (row == PACIFIC_ROW or col == PACIFIC_COL): 
                    pacific = True

                if (row == ATLANTIC_ROW - 1 or col == ATLANTIC_COL - 1): 
                    atlantic = True

                # look at all neighbours
                for dx, dy in directions:
                    if ((PACIFIC_ROW <= row + dx < ATLANTIC_ROW and
                    PACIFIC_COL <= col + dy < ATLANTIC_COL and (row+dx, col+dy) not in visited)
                    and heights[row + dx][col + dy] <= heights[row][col]
                    ):
                        visited.add((row+dx, col+dy))
                        q.append((row+dx, col+dy))
                       

            return pacific and atlantic

        res = []
        for i in range(ATLANTIC_ROW):
            for j in range(ATLANTIC_COL):
                if bfs(i,j, set()):
                    res.append([i,j])

        return res




