class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board),len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r,c):
            nonlocal board
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O"):
                return

            board[r][c] = "#"
            for dx, dy in directions:
                dfs(r + dx, c + dy)


        for row in range(rows):
            dfs(row,0) 
            dfs(row,cols - 1)

        for col in range(cols):
            dfs(0,col) 
            dfs(rows - 1,col)

        for i in range(rows):
            for j in range(cols):
                match board[i][j]:
                    case "O":
                        board[i][j] = "X"
                    case "#":
                        board[i][j] = "O"
        print(board)
