class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        # base cases, if the 'O' are in a corner, do nothing


        # maybe check all of the border "O"'s to see if they have any adjacent O's.

        # If they do, then mark all of their neighbours, and they can't be surrounded

        # If they don't then those O's can be surrounded


        numRows, numCols = len(board), len(board[0])


        offset = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(i,j):
            if min(i,j) < 0 or i > numRows - 1 or j > numCols - 1 or board[i][j] != "O":
                return

            board[i][j] = "P"
            
            for x,y in offset:
                dfs(i + x, j + y)


        # loop through the first row, last row, first col, last col

        first_row = board[0]
        last_row = board[numRows - 1]

        first_column = [row[0] for row in board]
        last_column = [row[numCols - 1] for row in board]


        for index, row in enumerate(first_row):
            
            if board[0][index] == "O":
                dfs(0, index)

        for index, row in enumerate(last_row):
            if board[numRows - 1][index] == "O":
                dfs(numRows - 1, index)

        for index, column in enumerate(first_column):
            if board[index][0] == "O":
                dfs(numRows - 1, index)

        for index, column in enumerate(last_column):
            if board[index][numCols - 1] == "O":
                dfs(numRows - 1, index)


        
        for i in range(numRows):
            for j in range(numCols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"



            


            

            
            






