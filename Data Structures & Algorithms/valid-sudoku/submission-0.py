class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_duplicates(board)


    def check_duplicates(self, board):
        
        # check for rows for duplicates
        for row in board:
            row_set = set()
            for column in row:
                if column.isnumeric():
                    if column in row_set:
                        return False
                    row_set.add(column)

        for i in range(len(board[0])):
            column_set = set()
            for column in board:
                if column[i].isnumeric():
                    if column[i] in column_set:
                        return False
                    column_set.add(column[i])

        return True