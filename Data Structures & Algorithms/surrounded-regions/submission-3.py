class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # 
        def dfs(x, y):
            if x <= 0 or y <= 0 or x >= len(board) - 1 or y >= len(board[0]) - 1 or board[x][y] != "O":
                return

            board[x][y] = "Y"

            offsets = [(0,1), (1,0), (-1,0), (0,-1)]

            for offX, offY in offsets:
                dfs(x + offX, y + offY)

            # basically O's that are not in the border

        for row_num, row in enumerate(board):
            for col_num, element in enumerate(row):

                if element == "O":
                    dfs(row_num, col_num)

        for row_num, row in enumerate(board):
            for col_num, elt in enumerate(row):
                if elt == "Y":
                    board[row_num][col_num] = "X"
                    # elt = "X"


